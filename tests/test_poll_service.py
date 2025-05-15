import pytest
from scr.services.poll_service import PollService
from scr.repositories.poll_repository import PollRepository
from scr.repositories.nft_repository import NFTRepository
from scr.repositories.user_repository import UserRepository
from scr.patterns.strategy import AlphabeticalTieBreaker

@pytest.fixture
def poll_service():
    return PollService(PollRepository(), NFTRepository(), UserRepository(), AlphabeticalTieBreaker())

def test_create_poll(poll_service):
    poll_id = poll_service.create_poll("¿Mejor juego?", ["Minecraft", "Zelda"], 60)
    assert poll_id is not None

def test_vote_multiple_users(poll_service):
    poll_id = poll_service.create_poll("¿Mejor juego?", ["Minecraft", "Zelda"], 60)
    poll_service.vote(poll_id, "silvia", "Minecraft")
    poll_service.vote(poll_id, "juan", "Zelda")
    results = poll_service.get_partial_results(poll_id)
    assert results["Minecraft"] == 1
    assert results["Zelda"] == 1

def test_reject_duplicate_vote(poll_service):
    poll_id = poll_service.create_poll("¿Mejor juego?", ["Minecraft", "Zelda"], 60)
    poll_service.vote(poll_id, "silvia", "Minecraft")
    with pytest.raises(ValueError):
        poll_service.vote(poll_id, "silvia", "Zelda")

def test_auto_close_poll(poll_service, mocker):
    mocker.patch("src.models.poll.datetime", autospec=True)
    mocker.patch("src.models.poll.datetime.now", return_value=1234567890)
    poll_id = poll_service.create_poll("¿Mejor juego?", ["Minecraft", "Zelda"], 5)
    poll_service.check_and_close_polls()
    assert poll_service.get_final_results(poll_id) is not None
