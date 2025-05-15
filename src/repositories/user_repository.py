import json
import sqlite3
from src.models.user import User

class UserRepository:
    def __init__(self, storage_type='json', db_path='data/users.db', json_path='data/users.json'):
        self.storage_type = storage_type
        self.db_path = db_path
        self.json_path = json_path

    def save_user(self, user: User):
        if self.storage_type == 'json':
            self._save_user_json(user)
        elif self.storage_type == 'sqlite':
            self._save_user_sqlite(user)

    def _save_user_json(self, user: User):
        try:
            with open(self.json_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data[user.username] = {"password_hash": user.password_hash, "tokens": [t.token_id for t in user.tokens]}

        with open(self.json_path, 'w') as file:
            json.dump(data, file, indent=4)

    def _save_user_sqlite(self, user: User):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password_hash TEXT,
                tokens TEXT
            )
        """)
        cursor.execute("INSERT OR REPLACE INTO users VALUES (?, ?, ?)",
                       (user.username, user.password_hash, json.dumps([t.token_id for t in user.tokens])))
        conn.commit()
        conn.close()
