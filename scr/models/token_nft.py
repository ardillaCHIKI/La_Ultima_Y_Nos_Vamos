# src/models/token_nft.py
import uuid

class TokenNFT:
    def __init__(self, poll_id: str, option: str, owner_id: str):
        self.token_id = str(uuid.uuid4())
        self.poll_id = poll_id
        self.option = option
        self.owner_id = owner_id
