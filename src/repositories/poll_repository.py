import json
import sqlite3
from src.models.poll import Poll

class PollRepository:
    def __init__(self, storage_type='json', db_path='data/polls.db', json_path='data/polls.json'):
        self.storage_type = storage_type
        self.db_path = db_path
        self.json_path = json_path

    def save_poll(self, poll: Poll):
        if self.storage_type == 'json':
            self._save_poll_json(poll)
        elif self.storage_type == 'sqlite':
            self._save_poll_sqlite(poll)

    def _save_poll_json(self, poll: Poll):
        try:
            with open(self.json_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data[poll.poll_id] = poll.__dict__

        with open(self.json_path, 'w') as file:
            json.dump(data, file, indent=4)

    def _save_poll_sqlite(self, poll: Poll):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS polls (
                poll_id TEXT PRIMARY KEY,
                question TEXT,
                options TEXT,
                active INTEGER
            )
        """)
        cursor.execute("INSERT OR REPLACE INTO polls VALUES (?, ?, ?, ?)",
                       (poll.poll_id, poll.question, json.dumps(poll.options), int(poll.active)))
        conn.commit()
        conn.close()
