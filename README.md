# PostgreSQL to JSON Exporter

Этот проект позволяет выгружать данные из базы данных PostgreSQL в JSON файлы, используя Python и библиотеку psycopg2. Скрипт включает в себя использование контекстных менеджеров для подключения и выполнения запросов, а также функции для сохранения данных в JSON файл.
(Проект разработан в рамках тестового здания)

## Установка

1. Клонируйте репозиторий:

   ```sh
   git clone https://github.com/makamonstir/russiancompany_test_assignment.git
   cd russiancompany_test_assignment
   ```

2. Создайте виртуальное окружение и активируйте его:

   ```sh
   python -m venv venv
   myenv\Scripts\activate # Для Linux/MacOS: source myenv/bin/activate
   ```

3. Установка зависимостей:
   ```sh
   pip install --upgrade pip && pip install -r requirements.txt
   ```

## Использование

Для запуска скрипта используйте команду:

```sh
python main.py --dbname your_db_name --user your_username --password your_password --host your_host --port your_port --query "SELECT * FROM your_table WHERE column_name = %s" --params values --output output.json
```

Параметры:

    --dbname: Имя базы данных
    --user: Имя пользователя
    --password: Пароль
    --host: Хост
    --port: Порт
    --query: SQL-запрос для выполнения
    --params: Параметры для SQL-запроса
    --output: Путь к выходному JSON файлу
