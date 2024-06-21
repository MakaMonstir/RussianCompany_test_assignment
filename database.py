import psycopg2
import logging
from contextlib import contextmanager
from psycopg2 import extensions
from typing import List, Optional, Dict

@contextmanager
def get_db_connection(connection_params: Optional[Dict]):
    """
    Генератор для контекстного менеджера подключения к базе данных.

    :param connection_params: Параметры подключения к базе данных.
    :yield: Объект соединения с базой данных.
    """
    connection: Optional[extensions.connection] = None
    try:
        logging.info("Установка соединения с базой данных")
        connection = psycopg2.connect(**connection_params)
        yield connection
    except psycopg2.DatabaseError as e:
        logging.error(f"Ошибка при подключение к базе данных: {e}")
        raise
    finally:
        if connection is not None:
            connection.close()
            logging.info("Соединение с базой данных закрыто")


def get_data_from_db(query: str, params, connection_params: Optional[List]) -> List[dict]:
    '''
    Функция для извлечения данных из PostgreSQL.

    :param query: SQL-запрос для выполнения.
    :param params: Параметры для SQL-запроса.
    :param connection_params: Параметры подключения к базе данных.
    :return: Список словарей с данными.
    '''

    with get_db_connection(connection_params) as connection:
        cursor: extensions.cursor = connection.cursor()
        logging.info(f"Выполнение запроса: {query}")
        cursor.execute(query=query, vars=params)
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        logging.info("Приведение данных к формату JSON")
        data = [dict(zip(columns, row)) for row in rows]
        return data
