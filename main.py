import os
import argparse
from database import get_data_from_db
from json_utils import save_data_to_json
from logger import setup_logging

def validate_args(args) -> None:
    """
    Функция для валидации аргументов командной строки
    """
    if not os.path.exists(os.path.dirname(args.output)):
        raise argparse.ArgumentTypeError(f"Не существует пути: {args.output}")
    

def main():
    setup_logging()

    args_parser = argparse.ArgumentParser(description="Выгрузка данных из PostgreSQL в JSON файл")

    args_parser.add_argument("--dbname", required=True, help="Имя базы данных")
    args_parser.add_argument("--user", required=True, help="Имя пользователя")
    args_parser.add_argument("--password", required=True, help="Пароль")
    args_parser.add_argument("--host", required=True, help="Хост")
    args_parser.add_argument("--port", required=True, help="Порт")
    args_parser.add_argument("--query", required=True, help="SQL-запрос для выполнения")
    args_parser.add_argument("--params", nargs='*', help="Параметры для SQL-запроса")
    args_parser.add_argument("--output", required=True, help="Путь к выходному JSON-файлу")

    args = args_parser.parse_args()

    validate_args(args)

    connection_params = {
        "dbname":args.dbname,
        "user":args.user,
        "password":args.password,
        "host":args.host,
        "port":args.port,
    }

    query_params = tuple(args.params) if args.params else ()
    data = get_data_from_db(query=args.query, params=query_params, connection_params=connection_params)
    if data:
        save_data_to_json(data=data, file_path=args.output)

if __name__ == "__main__":
    main()