# src/models/user.py
from src.models.token_nft import TokenNFT
class User:
    def __init__(self, username: str, password_hash: str):
        self.username = username
        self.password_hash = password_hash
        self.tokens = []

    def add_token(self, token: TokenNFT):
        self.tokens.append(token)
