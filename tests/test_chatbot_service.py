import pytest
from src.services.chatbot_service import ChatbotService
from src.services.poll_service import PollService
from src.repositories.poll_repository import PollRepository

@pytest.fixture
def chatbot_service():
    poll_service = PollService(PollRepository())
    return ChatbotService(poll_service)

def test_poll_question(chatbot_service):
    response = chatbot_service.respond_to_message("silvia", "¿Quién va ganando?")
    assert "resultado" in response

def test_pipeline_mock(mocker, chatbot_service):
    mocker.patch.object(chatbot_service.chatbot, "__call__", return_value=[{"generated_text": "Prueba de respuesta IA"}])
    response = chatbot_service.respond_to_message("silvia", "¿Cómo estás?")
    assert response == "Prueba de respuesta IA"
