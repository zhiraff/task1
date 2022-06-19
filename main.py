# Подключаем библиотеки
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from DBManager import UseDBPG
from pycbrf.toolbox import ExchangeRates
import time

CREDENTIALS_FILE = 'python-353709-3da98fbe12c2.json'  # Имя файла с закрытым ключом для работы с google api
spreadsheetId = '1BKzDMJvtj_jkJ7nPfaCu3uLPICUyzhJYii_3J9z0JCg'  #   Id документа, пполучен из url
ranges = ["Лист1!A2:D100"]  #   Диапазон ячеек для выборки, с запасом
course = 1.0  #   Курс доллара, по умолчанию 1
time_delay = 20  #   Время задержки между циклами в секундах
sheet_values = []   #   Значения ячеек в google sheet
counter = 1 #   Счётчик итераций главного цикла
# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth) # Выбираем работу с таблицами и 4 версию API

def get_data_from_google():
    """Делаем выборку из гугла"""
    global sheet_values
    print('Получение данных с google sheets...', end='')
    try:
        results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
        # получим значения выборки
        sheet_values = results['valueRanges'][0]['values']
        print('ok')
    except:
        print('error')

    # print(sheet_values)

def get_course():
    """вытащим курс доллара"""
    global course
    print('Получение курса доллара...', end='')
    try:
        rates = ExchangeRates()
        course = rates['USD'].value
        print('ok')
    except:
        print('error')

def update_db():
    """Обновим данные в таблице"""
    global sheet_values, course
    print('Обновление таблицы в БД...', end='')
    with UseDBPG() as cursor:
        _SQL = """TRUNCATE TABLE ONLY cost_of_orders RESTART IDENTITY"""
        cursor.execute(_SQL)
        _SQL = """INSERT INTO cost_of_orders VALUES (%s, %s, %s, %s, %s)"""
        try:
            for item in sheet_values:
                cost_usd = float(item[2])
                cursor.execute(_SQL, (item[0], item[1], item[2], item[3], cost_usd*float(course)))
            print('ok')
        except:
            print('error')

if __name__ == '__main__':
    while(True):
        print('Обновление данных № ', counter)
        counter += 1
        get_data_from_google()
        get_course()
        update_db()
        print('следующее обновление через ', time_delay, 'сек.')
        print('Для выхода нажмите CTRL+C')
        time.sleep(time_delay)
