"""Вспомогательный модуль для работы с БД"""
import psycopg2

dbconfig = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '1',
    'database': 'task1'
}

class UseDBPG():
    """Протокол управления контекстом, для работы с БД Postgresql"""
    def __init__(self, config: dict=dbconfig) -> None:
        self.config = config

    def __enter__(self) -> 'cursor':
        self.conn = psycopg2.connect(**self.config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

def test(dbconfig=dbconfig):
    conn = psycopg2.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL="""SELECT * FROM cost_of_orders"""
    cursor.execute(_SQL,)
    for item in cursor.fetchall():
        print(item)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    test()