import sqlite3

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect('logs.db', check_same_thread=False)
            cls._instance.create_table()
        return cls._instance

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, event TEXT, details TEXT)''')
        self.connection.commit()

    def get_connection(self):
        return self.connection