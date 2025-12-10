from database import Database

class LogRepository:
    def __init__(self):
        self.db = Database().get_connection()

    def save_log(self, event, details):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO logs (event, details) VALUES (?, ?)", (event, details))
        self.db.commit()