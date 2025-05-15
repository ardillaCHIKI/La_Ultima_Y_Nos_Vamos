import json
import sqlite3
from models.token_nft import TokenNFT

class NFTRepository:
    def __init__(self, storage_type='json', db_path='data/nfts.db', json_path='data/nfts.json'):
        self.storage_type = storage_type
        self.db_path = db_path
        self.json_path = json_path

    def save_token(self, token: TokenNFT):
        if self.storage_type == 'json':
            self._save_token_json(token)
        elif self.storage_type == 'sqlite':
            self._save_token_sqlite(token)

    def _save_token_json(self, token: TokenNFT):
        try:
            with open(self.json_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data[token.token_id] = {
            "poll_id": token.poll_id,
            "option": token.option,
            "owner_id": token.owner_id
        }

        with open(self.json_path, 'w') as file:
            json.dump(data, file, indent=4)

    def _save_token_sqlite(self, token: TokenNFT):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tokens (
                token_id TEXT PRIMARY KEY,
                poll_id TEXT,
                option TEXT,
                owner_id TEXT
            )
        """)
        cursor.execute("INSERT OR REPLACE INTO tokens VALUES (?, ?, ?, ?)",
                       (token.token_id, token.poll_id, token.option, token.owner_id))
        conn.commit()
        conn.close()
