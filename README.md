# task1

Инструкция по запуску

1. Установить модули Python из файла requirements.txt 
    $ pip install -r requirements.txt
2. Создать таблицу в локальной БД Postgresql используя дамп task1.sql (сама СУБД Postgresql должна быть уже установлена) 
    $ psql --username {{Имя польз. БД., наприм. postgres}} {{имя БД, наприм. task1}} < task1.sql
3. В файле DBManager.py прописать настройки подключения к локальной БД, в словаре 
    dbconfig = {
        'host': 'localhost',
        'user': 'postgres',
        'password': '1',
        'database': 'task1'
    }
4. В файле main.py указать путь и название Вашего файла с ключами от google sheets
    CREDENTIALS_FILE = 'python-353709-3da98fbe12c2.json'

5. Запускать главный скрипт 
    $ python main.py
