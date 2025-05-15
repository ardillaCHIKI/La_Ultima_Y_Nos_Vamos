from src.models.token_nft import TokenNFT

class TokenFactory:
    @staticmethod
    def create_token(poll_id: str, option: str, owner_id: str, edition="standard"):
        return TokenNFT(poll_id, option, owner_id)
