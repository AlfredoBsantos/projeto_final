from database import Database

class UserRepository:
    def __init__(self):
        self.db = Database().get_connection()

    def save(self, name, email):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self.db.commit()
        return cursor.lastrowid