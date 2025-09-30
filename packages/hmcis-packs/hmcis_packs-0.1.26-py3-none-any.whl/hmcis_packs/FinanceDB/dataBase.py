import csv
import io
import os
import tempfile
import time
from contextlib import contextmanager

import numpy as np
import pandas as pd
import psycopg2
import yaml

from hmcis_packs.logger.logger_config import setup_logger

logger = setup_logger(__name__)


class ReallyOptimizedDatabaseClient:
    def __init__(self, config_path=None):
        if config_path is None:
            user_home = os.path.expanduser("~")
            config_path = os.path.join(user_home, "db_config.yaml")

        with open(config_path, 'r', encoding='utf-8') as f:
            self.db_config = yaml.safe_load(f)

    @contextmanager
    def get_speed_optimized_connection(self):
        """Подключение с оптимизированными настройками для скорости"""
        conn = psycopg2.connect(**self.db_config)

        try:
            with conn.cursor() as cur:
                # Только настройки, которые МОЖНО менять во время сессии
                try:
                    cur.execute("SET synchronous_commit = OFF")  # Асинхронные коммиты
                    cur.execute("SET maintenance_work_mem = '512MB'")  # Память для операций
                    cur.execute("SET work_mem = '256MB'")  # Память для сортировок
                    cur.execute("SET temp_buffers = '64MB'")  # Буферы для временных таблиц
                    # cur.execute("SET commit_delay = 1000")           # Задержка коммита для группировки
                    cur.execute("SET commit_siblings = 5")  # Минимум транзакций для группировки

                    # Эти параметры могут не поддерживаться в некоторых версиях
                    try:
                        cur.execute("SET checkpoint_completion_target = 0.9")
                    except psycopg2.Error:
                        pass

                    logger.info("✅ Применены оптимизированные настройки PostgreSQL")
                except psycopg2.Error as e:
                    logger.warning(f"⚠️  Некоторые настройки PostgreSQL не применены: {e}")
                    # Продолжаем работу даже если настройки не применились

                conn.commit()

            yield conn

        finally:
            # Возвращаем безопасные настройки (только те, что можно менять)
            try:
                with conn.cursor() as cur:
                    cur.execute("SET synchronous_commit = ON")
                    conn.commit()
            except:
                pass
            conn.close()

    @contextmanager
    def get_safe_optimized_connection(self):
        """Подключение с безопасными оптимизациями (без server-level параметров)"""
        conn = psycopg2.connect(**self.db_config)

        try:
            with conn.cursor() as cur:
                # Только session-level настройки, которые точно работают
                cur.execute("SET synchronous_commit = OFF")  # Асинхронные коммиты
                cur.execute("SET maintenance_work_mem = '256MB'")  # Память для операций
                cur.execute("SET work_mem = '128MB'")  # Память для сортировок
                logger.info("✅ Применены безопасные оптимизации PostgreSQL")

            yield conn

        finally:
            try:
                with conn.cursor() as cur:
                    cur.execute("SET synchronous_commit = ON")
            except:
                pass
            conn.close()

    def _get_optimized_pg_type(self, pandas_dtype):
        """Быстрый маппинг типов с оптимальными PostgreSQL типами"""
        dtype_str = str(pandas_dtype).lower()

        # Специальная обработка datetime64[ns] - основного типа pandas для дат
        if 'datetime64' in dtype_str:
            if '[ns]' in dtype_str:  # datetime64[ns] - наносекунды
                return 'TIMESTAMP WITHOUT TIME ZONE'
            elif '[us]' in dtype_str:  # datetime64[us] - микросекунды
                return 'TIMESTAMP WITHOUT TIME ZONE'
            elif '[ms]' in dtype_str:  # datetime64[ms] - миллисекунды
                return 'TIMESTAMP WITHOUT TIME ZONE'
            else:
                return 'TIMESTAMP WITHOUT TIME ZONE'

        # Проверяем pandas API для datetime типов (более надежно)
        if pd.api.types.is_datetime64_any_dtype(pandas_dtype):
            return 'TIMESTAMP WITHOUT TIME ZONE'

        # Дополнительная проверка для timezone-aware datetime
        if hasattr(pandas_dtype, 'tz') and pandas_dtype.tz is not None:
            return 'TIMESTAMP WITH TIME ZONE'

        # Остальные типы
        if 'int8' in dtype_str or 'int16' in dtype_str:
            return 'SMALLINT'
        elif 'int32' in dtype_str:
            return 'INTEGER'
        elif 'int64' in dtype_str or 'int' in dtype_str:
            return 'BIGINT'
        elif 'float32' in dtype_str:
            return 'REAL'
        elif 'float64' in dtype_str or 'float' in dtype_str:
            return 'DOUBLE PRECISION'  # Быстрее чем NUMERIC
        elif 'bool' in dtype_str:
            return 'BOOLEAN'
        elif 'datetime' in dtype_str or 'timestamp' in dtype_str:
            return 'TIMESTAMP WITHOUT TIME ZONE'
        elif 'object' in dtype_str:
            return 'TEXT'
        else:
            return 'TEXT'

    def save_with_temp_file_copy(self,
                                 df: pd.DataFrame,
                                 table_name: str,
                                 schema: str = 'IFRS Reports') -> None:
        """
        САМЫЙ БЫСТРЫЙ метод: временный TSV файл + PostgreSQL COPY
        """
        start_time = time.time()
        total_rows = len(df)

        # Быстрая предобработка
        df_clean = df.dropna(axis=1, how='all')  # Удаляем полностью пустые колонки
        df_clean = df_clean.loc[:, df_clean.columns.str.strip() != '']  # Удаляем колонки с пустыми именами

        logger.info(f"🚀 COPY через временный файл: {total_rows:,} строк...")

        with self.get_speed_optimized_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    prep_start = time.time()

                    # 1. БЫСТРОЕ создание схемы (без проверок)
                    try:
                        cursor.execute(f'CREATE SCHEMA "{schema}"')
                    except psycopg2.Error:
                        pass  # Схема уже существует

                    # 2. БЫСТРОЕ создание таблицы
                    column_definitions = []
                    for col_name, dtype in zip(df_clean.columns, df_clean.dtypes):
                        pg_type = self._get_optimized_pg_type(dtype)
                        # Экранируем имена колонок
                        safe_col_name = col_name.replace('"', '""')
                        column_definitions.append(f'"{safe_col_name}" {pg_type}')

                    # ДРОПАЕМ таблицу без проверок (быстрее чем TRUNCATE)
                    cursor.execute(f'DROP TABLE IF EXISTS "{schema}"."{table_name}"')

                    # Создаем UNLOGGED таблицу (БЕЗ WAL логирования = супер быстро)
                    create_table_sql = f'''
                    CREATE UNLOGGED TABLE "{schema}"."{table_name}" (
                        {', '.join(column_definitions)}
                    )
                    '''
                    cursor.execute(create_table_sql)

                    prep_time = time.time() - prep_start
                    logger.info(f"⚡ Подготовка таблицы: {prep_time:.2f}с")

                    # 3. БЫСТРАЯ подготовка данных
                    data_start = time.time()

                    # Заменяем NaN на None ВЕКТОРНО (самый быстрый способ)
                    df_for_export = df_clean.where(pd.notnull(df_clean), None)

                    # Создаем временный TSV файл
                    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.tsv',
                                                     encoding='utf-8') as tmp_file:
                        writer = csv.writer(tmp_file, delimiter='\t', quoting=csv.QUOTE_MINIMAL,
                                            lineterminator='\n', quotechar='"')

                        # Пишем данные построчно (быстрее чем DataFrame.to_csv для больших данных)
                        for row in df_for_export.values:
                            processed_row = []
                            for val in row:
                                if val is None:
                                    processed_row.append('')  # Пустая строка для NULL
                                elif isinstance(val, str):
                                    # Минимальное экранирование только критичных символов
                                    processed_row.append(val.replace('\t', ' ').replace('\r\n', ' ').replace('\n', ' '))
                                else:
                                    processed_row.append(str(val))
                            writer.writerow(processed_row)

                        temp_file_path = tmp_file.name

                    data_time = time.time() - data_start
                    logger.info(f"⚡ Подготовка данных: {data_time:.2f}с")

                    # 4. СУПЕР-БЫСТРЫЙ COPY из файла
                    copy_start = time.time()

                    # Формируем список колонок для COPY
                    column_names = []
                    columns_sql = ', '.join(column_names)

                    # COPY команда с оптимальными настройками
                    copy_command = f'''
                    COPY "{schema}"."{table_name}" ({columns_sql})
                    FROM '{temp_file_path}'
                    WITH (
                        FORMAT CSV,
                        DELIMITER E'\\t',
                        NULL '',
                        HEADER false,
                        QUOTE '"'
                    )
                    '''

                    cursor.execute(copy_command)

                    # Удаляем временный файл
                    try:
                        os.unlink(temp_file_path)
                    except:
                        pass

                    copy_time = time.time() - copy_start
                    logger.info(f"⚡ COPY из файла: {copy_time:.2f}с")

                    # 5. ОДИН коммит в самом конце
                    commit_start = time.time()
                    conn.commit()
                    commit_time = time.time() - commit_start
                    logger.info(f"⚡ Коммит: {commit_time:.2f}с")

                    # 6. Превращаем таблицу в обычную (с логированием) для надежности
                    cursor.execute(f'ALTER TABLE "{schema}"."{table_name}" SET LOGGED')
                    conn.commit()

                    # Итоговая статистика
                    total_time = time.time() - start_time
                    rows_per_second = total_rows / total_time if total_time > 0 else 0

                    logger.info(f"✅ COPY загрузка завершена:")
                    logger.info(f"   📊 Строк: {total_rows:,}")
                    logger.info(f"   ⏱️  Общее время: {total_time:.2f}с")
                    logger.info(f"   🚄 Скорость: {rows_per_second:,.0f} строк/сек")
                    logger.info(f"   🎯 Цель для 900K: {900000 / rows_per_second:.1f}с")

                except Exception as e:
                    conn.rollback()
                    logger.error(f"💀 Ошибка COPY загрузки: {e}")
                    # Очищаем временный файл при ошибке
                    try:
                        if 'temp_file_path' in locals():
                            os.unlink(temp_file_path)
                    except:
                        pass
                    raise

    def save_with_execute_values_turbo(self,
                                       df: pd.DataFrame,
                                       table_name: str,
                                       schema: str = 'IFRS Reports',
                                       batch_size: int = 50000) -> None:
        """
        Турбо-версия execute_values с максимальными оптимизациями
        """
        start_time = time.time()
        total_rows = len(df)

        df_clean = df.dropna(axis=1, how='all')
        df_clean = df_clean.loc[:, df_clean.columns.str.strip() != '']

        logger.info(f"⚡ Execute_values ТУРБО: {total_rows:,} строк...")

        with self.get_speed_optimized_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    # Быстрая подготовка схемы и таблицы
                    try:
                        cursor.execute(f'CREATE SCHEMA "{schema}"')
                    except psycopg2.Error:
                        pass

                    column_definitions = []
                    for col_name, dtype in zip(df_clean.columns, df_clean.dtypes):
                        pg_type = self._get_optimized_pg_type(dtype)
                        safe_col_name = col_name.replace('"', '""')
                        column_definitions.append(f'"{safe_col_name}" {pg_type}')

                    cursor.execute(f'DROP TABLE IF EXISTS "{schema}"."{table_name}"')

                    create_table_sql = f'''
                    CREATE UNLOGGED TABLE "{schema}"."{table_name}" (
                        {', '.join(column_definitions)}
                    )
                    '''
                    cursor.execute(create_table_sql)

                    # Подготовка данных ВЕКТОРНО
                    df_for_insert = df_clean.where(pd.notnull(df_clean), None)
                    all_records = [tuple(row) for row in df_for_insert.values]

                    # МЕГА execute_values с огромными батчами
                    column_names = [f'"{col.replace('"', '""')}"' for col in df_clean.columns]
                    columns_sql = ', '.join(column_names)

                    insert_sql = f'''
                    INSERT INTO "{schema}"."{table_name}" ({columns_sql}) VALUES %s
                    '''

                    insert_start = time.time()

                    # Вставляем ОГРОМНЫМИ батчами
                    from psycopg2.extras import execute_values

                    if len(all_records) <= batch_size:
                        # Если данных немного - одним махом
                        execute_values(
                            cursor,
                            insert_sql,
                            all_records,
                            template=None,
                            page_size=len(all_records),  # Весь батч сразу
                            fetch=False
                        )
                    else:
                        # Большими кусками
                        for i in range(0, len(all_records), batch_size):
                            batch = all_records[i:i + batch_size]
                            execute_values(
                                cursor,
                                insert_sql,
                                batch,
                                template=None,
                                page_size=len(batch),
                                fetch=False
                            )
                            logger.info(f"📦 Батч {i // batch_size + 1}: {len(batch):,} строк")

                    insert_time = time.time() - insert_start
                    logger.info(f"⚡ Execute_values: {insert_time:.2f}с")

                    # Коммит и финализация
                    conn.commit()
                    cursor.execute(f'ALTER TABLE "{schema}"."{table_name}" SET LOGGED')
                    conn.commit()

                    total_time = time.time() - start_time
                    rows_per_second = total_rows / total_time if total_time > 0 else 0

                    logger.info(f"✅ Execute_values ТУРБО завершен:")
                    logger.info(f"   📊 Строк: {total_rows:,}")
                    logger.info(f"   ⏱️  Время: {total_time:.2f}с")
                    logger.info(f"   🚄 Скорость: {rows_per_second:,.0f} строк/сек")

                except Exception as e:
                    conn.rollback()
                    logger.error(f"💀 Ошибка Execute_values ТУРБО: {e}")
                    raise

    def save_with_copy_from_stringio(self,
                                     df: pd.DataFrame,
                                     table_name: str,
                                     schema: str = 'IFRS Reports') -> None:
        """
        COPY через StringIO (оптимизированная версия вашего оригинального подхода)
        """
        start_time = time.time()
        total_rows = len(df)

        df_clean = df.dropna(axis=1, how='all')
        df_clean = df_clean.loc[:, df_clean.columns.str.strip() != '']

        logger.info(f"📝 COPY через StringIO: {total_rows:,} строк...")

        with self.get_speed_optimized_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    # Подготовка таблицы
                    try:
                        cursor.execute(f'CREATE SCHEMA "{schema}"')
                    except psycopg2.Error:
                        pass

                    column_definitions = []
                    for col_name, dtype in zip(df_clean.columns, df_clean.dtypes):
                        pg_type = self._get_optimized_pg_type(dtype)
                        safe_col_name = col_name.replace('"', '""')
                        column_definitions.append(f'"{safe_col_name}" {pg_type}')

                    cursor.execute(f'DROP TABLE IF EXISTS "{schema}"."{table_name}"')

                    create_table_sql = f'''
                    CREATE UNLOGGED TABLE "{schema}"."{table_name}" (
                        {', '.join(column_definitions)}
                    )
                    '''
                    cursor.execute(create_table_sql)

                    # Оптимизированная подготовка StringIO
                    data_start = time.time()

                    # Быстрая замена NaN
                    df_copy = df_clean.fillna('')  # Пустая строка вместо \N (быстрее)

                    # Создаем StringIO с оптимальным размером буфера
                    output = io.StringIO()

                    # Используем pandas to_csv с оптимизированными параметрами
                    df_copy.to_csv(
                        output,
                        sep='\t',
                        header=False,
                        index=False,
                        na_rep='',
                        quoting=csv.QUOTE_MINIMAL,
                        lineterminator='\n'
                    )
                    output.seek(0)

                    data_time = time.time() - data_start
                    logger.info(f"⚡ Подготовка StringIO: {data_time:.2f}с")

                    # COPY из StringIO
                    copy_start = time.time()

                    column_names = [f'"{col.replace('"', '""')}"' for col in df_clean.columns]
                    columns_sql = ', '.join(column_names)

                    copy_command = f'''
                    COPY "{schema}"."{table_name}" ({columns_sql})
                    FROM STDIN
                    WITH (
                        FORMAT CSV,
                        DELIMITER E'\\t',
                        NULL '',
                        HEADER false
                    )
                    '''

                    cursor.copy_expert(copy_command, output)

                    copy_time = time.time() - copy_start
                    logger.info(f"⚡ COPY StringIO: {copy_time:.2f}с")

                    conn.commit()
                    cursor.execute(f'ALTER TABLE "{schema}"."{table_name}" SET LOGGED')
                    conn.commit()

                    total_time = time.time() - start_time
                    rows_per_second = total_rows / total_time if total_time > 0 else 0

                    logger.info(f"✅ COPY StringIO завершен:")
                    logger.info(f"   📊 Строк: {total_rows:,}")
                    logger.info(f"   ⏱️  Время: {total_time:.2f}с")
                    logger.info(f"   🚄 Скорость: {rows_per_second:,.0f} строк/сек")

                except Exception as e:
                    conn.rollback()
                    logger.error(f"💀 Ошибка COPY StringIO: {e}")
                    raise

    def save_with_copy_from_stringio_safe(self,
                                          df: pd.DataFrame,
                                          table_name: str,
                                          schema: str = 'IFRS Reports') -> None:
        """
        БЕЗОПАСНАЯ версия COPY через StringIO (без проблемных настроек)
        """
        start_time = time.time()
        total_rows = len(df)

        df_clean = df.dropna(axis=1, how='all')
        df_clean = df_clean.loc[:, df_clean.columns.str.strip() != '']

        logger.info(f"📝 БЕЗОПАСНЫЙ COPY через StringIO: {total_rows:,} строк...")

        with self.get_safe_optimized_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    # Подготовка таблицы
                    try:
                        cursor.execute(f'CREATE SCHEMA IF NOT EXISTS "{schema}"')
                    except psycopg2.Error:
                        pass

                    column_definitions = []
                    for col_name, dtype in zip(df_clean.columns, df_clean.dtypes):
                        pg_type = self._get_optimized_pg_type(dtype)
                        safe_col_name = col_name.replace('"', '""')
                        column_definitions.append(f'"{safe_col_name}" {pg_type}')

                    cursor.execute(f'DROP TABLE IF EXISTS "{schema}"."{table_name}"')

                    # Обычная таблица (не UNLOGGED для надежности)
                    create_table_sql = f'''
                    CREATE TABLE "{schema}"."{table_name}" (
                        {', '.join(column_definitions)}
                    )
                    '''
                    cursor.execute(create_table_sql)

                    # Оптимизированная подготовка StringIO
                    data_start = time.time()

                    # Быстрая замена NaN
                    df_copy = df_clean.fillna('')  # Пустая строка вместо \N

                    # Создаем StringIO с оптимальным размером буфера
                    output = io.StringIO()

                    # Используем pandas to_csv с оптимизированными параметрами
                    df_copy.to_csv(
                        output,
                        sep='\t',
                        header=False,
                        index=False,
                        na_rep='',
                        quoting=csv.QUOTE_MINIMAL,
                        lineterminator='\n',
                        escapechar='\\',
                        doublequote=True
                    )
                    output.seek(0)

                    data_time = time.time() - data_start
                    logger.info(f"⚡ Подготовка StringIO: {data_time:.2f}с")

                    # COPY из StringIO
                    copy_start = time.time()

                    column_names = [f'"{col.replace('"', '""')}"' for col in df_clean.columns]
                    columns_sql = ', '.join(column_names)

                    copy_command = f'''
                    COPY "{schema}"."{table_name}" ({columns_sql})
                    FROM STDIN
                    WITH (
                        FORMAT CSV,
                        DELIMITER E'\\t',
                        NULL '',
                        HEADER false,
                        QUOTE '"',
                        ESCAPE '\\'
                    )
                    '''

                    cursor.copy_expert(copy_command, output)

                    copy_time = time.time() - copy_start
                    logger.info(f"⚡ COPY StringIO: {copy_time:.2f}с")

                    conn.commit()

                    total_time = time.time() - start_time
                    rows_per_second = total_rows / total_time if total_time > 0 else 0

                    logger.info(f"✅ БЕЗОПАСНЫЙ COPY StringIO завершен:")
                    logger.info(f"   📊 Строк: {total_rows:,}")
                    logger.info(f"   ⏱️  Время: {total_time:.2f}с")
                    logger.info(f"   🚄 Скорость: {rows_per_second:,.0f} строк/сек")
                    logger.info(f"   🎯 Для 900K строк потребуется: {(900000 / rows_per_second):.1f}с")

                except Exception as e:
                    conn.rollback()
                    logger.error(f"💀 Ошибка БЕЗОПАСНОГО COPY StringIO: {e}")
                    raise

    def save_ultra_safe(self,
                        df: pd.DataFrame,
                        table_name: str,
                        schema: str = 'IFRS Reports') -> None:
        """
        УЛЬТРА-БЕЗОПАСНАЯ версия без каких-либо оптимизаций PostgreSQL
        Гарантированно работает везде, но может быть медленнее
        """
        start_time = time.time()
        total_rows = len(df)

        df_clean = df.dropna(axis=1, how='all')
        df_clean = df_clean.loc[:, df_clean.columns.str.strip() != '']

        logger.info(f"🔒 УЛЬТРА-БЕЗОПАСНАЯ загрузка: {total_rows:,} строк...")

        with self.get_safe_optimized_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    # Подготовка таблицы
                    cursor.execute(f'CREATE SCHEMA IF NOT EXISTS "{schema}"')

                    column_definitions = []
                    for col_name, dtype in zip(df_clean.columns, df_clean.dtypes):
                        pg_type = self._get_optimized_pg_type(dtype)
                        safe_col_name = col_name.replace('"', '""')
                        column_definitions.append(f'"{safe_col_name}" {pg_type}')

                    cursor.execute(f'DROP TABLE IF EXISTS "{schema}"."{table_name}"')

                    # Обычная таблица (без UNLOGGED)
                    create_table_sql = f'''
                    CREATE TABLE "{schema}"."{table_name}" (
                        {', '.join(column_definitions)}
                    )
                    '''
                    cursor.execute(create_table_sql)

                    # Простая подготовка StringIO
                    data_start = time.time()
                    df_copy = df_clean.fillna('')

                    output = io.StringIO()
                    df_copy.to_csv(
                        output,
                        sep='\t',
                        header=False,
                        index=False,
                        na_rep='',
                        lineterminator='\n'
                    )
                    output.seek(0)

                    data_time = time.time() - data_start
                    logger.info(f"⚡ Подготовка данных: {data_time:.2f}с")

                    # Простой COPY
                    copy_start = time.time()

                    column_names = [f'"{col.replace('"', '""')}"' for col in df_clean.columns]
                    columns_sql = ', '.join(column_names)

                    copy_command = f'''
                    COPY "{schema}"."{table_name}" ({columns_sql})
                    FROM STDIN
                    WITH CSV DELIMITER E'\\t' NULL ''
                    '''

                    cursor.copy_expert(copy_command, output)

                    copy_time = time.time() - copy_start
                    logger.info(f"⚡ COPY операция: {copy_time:.2f}с")

                    conn.commit()

                    total_time = time.time() - start_time
                    rows_per_second = total_rows / total_time if total_time > 0 else 0

                    logger.info(f"✅ УЛЬТРА-БЕЗОПАСНАЯ загрузка завершена:")
                    logger.info(f"   📊 Строк: {total_rows:,}")
                    logger.info(f"   ⏱️  Время: {total_time:.2f}с")
                    logger.info(f"   🚄 Скорость: {rows_per_second:,.0f} строк/сек")
                    logger.info(f"   🎯 Для 900K строк потребуется: {(900000 / rows_per_second):.1f}с")

                except Exception as e:
                    conn.rollback()
                    logger.error(f"💀 Ошибка УЛЬТРА-БЕЗОПАСНОЙ загрузки: {e}")
                    raise

    # Оригинальные методы для обратной совместимости
    def fetch_data(self, query: str, params: tuple = None, schema: str = None):
        conn = None
        try:
            conn = psycopg2.connect(**self.db_config)
            with conn.cursor() as cur:
                cur.execute(query, params)
                return cur.fetchall()
        except Exception as e:
            logger.error(f"Ошибка при работе с БД: {e}")
            return []
        finally:
            if conn:
                conn.close()


def benchmark_all_methods(test_df, client):
    """Полный бенчмарк всех методов (включая безопасные версии)"""

    methods = [
        ('🛡️  БЕЗОПАСНЫЙ COPY StringIO',
         lambda: client.save_with_copy_from_stringio_safe(test_df.copy(), 'benchmark_safe_stringio')),
        ('⚡ Execute_values ТУРБО',
         lambda: client.save_with_execute_values_turbo(test_df.copy(), 'benchmark_exec_turbo')),
        ('🚀 COPY через временный файл', lambda: client.save_with_temp_file_copy(test_df.copy(), 'benchmark_temp_file')),
        ('📝 COPY через StringIO (полный)',
         lambda: client.save_with_copy_from_stringio(test_df.copy(), 'benchmark_stringio')),
    ]

    results = []

    for method_name, method_func in methods:
        print(f"\n{'=' * 60}")
        print(f"🧪 ТЕСТ: {method_name}")
        print(f"{'=' * 60}")

        try:
            start = time.time()
            method_func()
            elapsed = time.time() - start
            rows_per_sec = len(test_df) / elapsed

            result = {
                'method': method_name,
                'time': elapsed,
                'rows_per_sec': rows_per_sec,
                'estimate_900k': (900000 / rows_per_sec) if rows_per_sec > 0 else 0
            }
            results.append(result)

            print(f"✅ РЕЗУЛЬТАТ:")
            print(f"   ⏱️  Время: {elapsed:.2f} секунд")
            print(f"   🚄 Скорость: {rows_per_sec:,.0f} строк/сек")
            print(f"   📊 Оценка для 900K строк: {result['estimate_900k']:.1f} сек")

        except Exception as e:
            print(f"❌ ОШИБКА: {e}")
            results.append({
                'method': method_name,
                'error': str(e)
            })

    # Итоговые результаты
    print(f"\n{'=' * 60}")
    print("🏆 ИТОГОВЫЕ РЕЗУЛЬТАТЫ")
    print(f"{'=' * 60}")

    successful = [r for r in results if 'error' not in r]
    if successful:
        best = min(successful, key=lambda x: x['time'])
        print(f"🥇 ЛУЧШИЙ: {best['method']}")
        print(f"   ⏱️  {best['time']:.2f}с для {len(test_df):,} строк")
        print(f"   📊 Оценка для 900K: {best['estimate_900k']:.1f}с")

        print(f"\n📈 ВСЕ РЕЗУЛЬТАТЫ:")
        for result in sorted(successful, key=lambda x: x['time']):
            print(f"   {result['method']}: {result['time']:.2f}с ({result['rows_per_sec']:,.0f} строк/сек)")

    return results


# Простая функция для быстрого использования
def quick_save_to_db(df: pd.DataFrame,
                     table_name: str,
                     schema: str = 'IFRS Reports',
                     method: str = 'safe') -> None:
    """
    Простая функция для быстрого сохранения DataFrame в БД

    Args:
        df: DataFrame для сохранения
        table_name: Имя таблицы
        schema: Схема БД
        method: Метод сохранения ('safe', 'fast', 'turbo', 'temp_file')
    """
    client = ReallyOptimizedDatabaseClient()

    if method == 'safe':
        client.save_with_copy_from_stringio_safe(df, table_name, schema)
    elif method == 'fast':
        client.save_with_copy_from_stringio(df, table_name, schema)
    elif method == 'turbo':
        client.save_with_execute_values_turbo(df, table_name, schema)
    elif method == 'temp_file':
        client.save_with_temp_file_copy(df, table_name, schema)
    else:
        raise ValueError("method должен быть одним из: 'safe', 'fast', 'turbo', 'temp_file'")


if __name__ == '__main__':
    # Тест с данными похожими на ваши XML
    print("🏗️  Создаем тестовый набор данных...")

    # Размер для быстрого тестирования (потом экстраполируем на 900K)
    test_size = 50000  # Уменьшенный размер для быстрого тестирования

    test_data = {
        'Delivery_Number': [f'DEL_{i:08d}' for i in range(test_size)],
        'Customer_Code': [f'CUST_{i % 10000:05d}' for i in range(test_size)],
        'Customer_Name': [f'Customer Company {i % 1000}' for i in range(test_size)],
        'Item_Code': [f'ITEM_{i % 50000:06d}' for i in range(test_size)],
        'Material_Number': [f'MAT_{i % 20000:07d}' for i in range(test_size)],
        'Material_Description': [f'Material Description for item {i}' for i in range(test_size)],
        'CAC_Code': [f'CAC_{i % 100:03d}' for i in range(test_size)],
        'SAC_Code': [f'SAC_{i % 200:03d}' for i in range(test_size)],
        'Segment_Code': [f'SEG_{i % 50:02d}' for i in range(test_size)],
        'Batch_Number': [f'BATCH_{i % 5000:06d}' for i in range(test_size)],
        'Country_Code': np.random.choice(['US', 'DE', 'CN', 'JP', 'KR', 'IN'], test_size),
        'Quantity': np.random.randint(1, 1000, test_size),
        'Unit_Price': np.random.uniform(0.01, 999.99, test_size),
        'Total_Amount': np.random.uniform(1.0, 50000.0, test_size),
        'Delivery_Date': pd.date_range('2024-01-01', periods=test_size, freq='5min'),
        'Status': np.random.choice(['ACTIVE', 'PENDING', 'SHIPPED', 'DELIVERED'], test_size)
    }

    test_df = pd.DataFrame(test_data)
    print(f"📊 Создан тестовый DataFrame: {len(test_df):,} строк × {len(test_df.columns)} колонок")
    print(f"💾 Размер в памяти: {test_df.memory_usage(deep=True).sum() / 1024 / 1024:.1f} MB")

    # Показываем типы данных
    print(f"\n📋 Типы данных:")
    for col, dtype in zip(test_df.columns, test_df.dtypes):
        print(f"   {col}: {dtype}")

    # Инициализируем клиент
    client = ReallyOptimizedDatabaseClient()

    # Быстрый тест одного метода
    print(f"\n🚀 БЫСТРЫЙ ТЕСТ (только безопасный метод)")
    print(f"{'=' * 60}")

    try:
        start_time = time.time()
        quick_save_to_db(test_df.copy(), 'quick_test', method='ultra_safe')
        elapsed = time.time() - start_time
        rows_per_sec = len(test_df) / elapsed
        estimate_900k = 900000 / rows_per_sec

        print(f"✅ БЫСТРЫЙ ТЕСТ ЗАВЕРШЕН:")
        print(f"   📊 Строк: {len(test_df):,}")
        print(f"   ⏱️  Время: {elapsed:.2f} секунд")
        print(f"   🚄 Скорость: {rows_per_sec:,.0f} строк/сек")
        print(f"   🎯 Оценка для 900K строк: {estimate_900k:.1f} секунд")

        if estimate_900k < 60:
            print(f"   🎉 ОТЛИЧНО! Ваши 900K строк загрузятся менее чем за минуту!")
        elif estimate_900k < 180:
            print(f"   👍 ХОРОШО! Ваши 900K строк загрузятся за {estimate_900k / 60:.1f} минуты")
        else:
            print(f"   ⚠️  Медленно. Попробуйте другой метод или оптимизируйте PostgreSQL")

    except Exception as e:
        print(f"❌ ОШИБКА БЫСТРОГО ТЕСТА: {e}")

    # Спрашиваем пользователя о полном бенчмарке
    print(f"\n❓ Запустить полный бенчмарк всех методов? (y/n): ", end="")
    try:
        user_input = input().lower()
        if user_input in ['y', 'yes', 'да', 'д']:
            print(f"\n🚀 ПОЛНЫЙ БЕНЧМАРК")
            benchmark_results = benchmark_all_methods(test_df, client)
        else:
            print("👍 Бенчмарк пропущен. Используйте quick_save_to_db() для быстрого сохранения!")
    except:
        print("👍 Бенчмарк пропущен. Используйте quick_save_to_db() для быстрого сохранения!")

# Пример использования для ваших XML данных:
"""
# После обработки XML в DataFrame:
from optimized_database_client import ReallyOptimizedDatabaseClient, quick_save_to_db

# Самый простой способ:
quick_save_to_db(df, 'xml_data', schema='XML_Import', method='safe')

# Или с полным контролем:
client = ReallyOptimizedDatabaseClient()
client.save_with_copy_from_stringio_safe(df, 'xml_deliveries', schema='XML_Import')

# Для максимальной скорости (если нет проблем с настройками PostgreSQL):
client.save_with_temp_file_copy(df, 'xml_deliveries', schema='XML_Import')
"""
