from decimal import Decimal
import json
import logging
from typing import Dict, List, Optional
from datetime import date

def save_data_to_json(data: List[Dict], file_path):
    """
    Функция сохранения данных в JSON-файл.

    :param data: Данные для сохранения.
    :param file_path: Путь для сохранения файла>
    """
    try:
        with open(file_path, 'w', encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=None, default=default_serializer)
        logging.info(f"Данные загружены в {file_path}")
    except IOError as error:
        logging.error("Ошибка при записи в файл: {error}")

def default_serializer(object: Optional[date|Decimal]) -> str:
    """
    Сериализатор для объектов с поддержкой типов, не встроенных в json сериализатор.
    """
    if isinstance(object, date):
        return object.strftime("%m/%d/%Y, %H:%M:%S")
    
    if isinstance(object, Decimal):
        return float(object)
    
    return str(object)