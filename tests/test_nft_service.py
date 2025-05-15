import pytest
from src.services.nft_service import NFTService
from src.repositories.nft_repository import NFTRepository

@pytest.fixture
def nft_service():
    return NFTService(NFTRepository())

def test_mint_token(nft_service):
    token = nft_service.mint_token("silvia", "poll123", "Minecraft")
    assert token.token_id is not None

def test_transfer_token(nft_service):
    token = nft_service.mint_token("silvia", "poll123", "Minecraft")
    assert nft_service.transfer_token(token.token_id, "juan") == True
