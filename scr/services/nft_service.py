from models.token_nft import TokenNFT
from repositories.nft_repository import NFTRepository

class NFTService:
    def __init__(self, nft_repository: NFTRepository):
        self.nft_repository = nft_repository

    def generate_token(self, poll_id: str, option: str, user_id: str):
        token = TokenNFT(poll_id, option, user_id)
        self.nft_repository.save_token(token)
        return token

    def transfer_token(self, token_id: str, new_owner_id: str):
        token = self.nft_repository.get_token(token_id)
        if token:
            token.owner_id = new_owner_id
            self.nft_repository.save_token(token)
        else:
            raise ValueError("Token no encontrado.")
