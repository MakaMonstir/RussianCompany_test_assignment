import json
import logging
from typing import Dict, List

def save_data_to_json(data: List[Dict], file_path):
    """
    Функция сохранения данных в JSON-файл.

    :param data: Данные для сохранения.
    :param file_path: Путь для сохранения файла>
    """
    try:
        with open(file_path, 'w', encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=None)
        logging.info(f"Данные загружены в {file_path}")
    except IOError as error:
        logging.error("Ошибка при записи в файл: {error}")
