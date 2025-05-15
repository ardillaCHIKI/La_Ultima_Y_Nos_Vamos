import uuid
from datetime import datetime
from src.models.poll import Poll
from src.models.vote import Vote
from src.repositories.poll_repository import PollRepository
from src.repositories.nft_repository import NFTRepository
from src.repositories.user_repository import UserRepository
from src.patterns.observer import Subject
from src.patterns.strategy import TieBreakerStrategy
from src.services.nft_service import NFTService

class PollService(Subject):
    def __init__(self, poll_repository: PollRepository, nft_repository: NFTRepository, user_repository: UserRepository, tiebreaker_strategy: TieBreakerStrategy):
        super().__init__()
        self.poll_repository = poll_repository
        self.nft_repository = nft_repository
        self.user_repository = user_repository
        self.tiebreaker_strategy = tiebreaker_strategy
        self.polls = {}

    def create_poll(self, question: str, options: list, duration_seconds: int, poll_type="simple"):
        poll_id = str(uuid.uuid4())
        poll = Poll(poll_id, question, options, duration_seconds)
        self.polls[poll_id] = poll
        self.poll_repository.save_poll(poll)
        return poll_id

    def vote(self, poll_id: str, username: str, option: str):
        # Verificar que la encuesta está activa y que el usuario no haya votado
        if not self.poll_repository.get_poll(poll_id).active:
            raise ValueError("Encuesta cerrada.")
        
        if self.poll_repository.user_has_voted(username, poll_id):
            raise ValueError("El usuario ya votó en esta encuesta.")

        # Registrar voto y guardar la encuesta actualizada
        self.poll_repository.register_vote(username, poll_id, option)

        # Generar NFT asociado al voto
        nft_token = self.nft_service.mint_token(username, poll_id, option)

        return f"Voto registrado. NFT generado: {nft_token.token_id}"

    def check_and_close_polls(self):
        now = datetime.now().timestamp()
        for poll_id, poll in self.polls.items():
            if poll.active and now > poll.end_time:
                self.close_poll(poll_id)

    def close_poll(self, poll_id: str):
        if poll_id not in self.polls:
            raise ValueError("Encuesta no encontrada.")

        poll = self.polls[poll_id]
        poll.active = False
        self.poll_repository.save_poll(poll)

        # Notificar observadores (NFTService, UIController, ChatbotService)
        self.notify_observers("poll_closed", {"poll_id": poll_id})

        return "Encuesta cerrada correctamente."

    def get_partial_results(self, poll_id: str):
        if poll_id not in self.polls:
            raise ValueError("Encuesta no encontrada.")
        return self.polls[poll_id].calculate_results()

    def get_final_results(self, poll_id: str):
        if poll_id not in self.polls or self.polls[poll_id].active:
            raise ValueError("La encuesta aún está activa.")
        return self.polls[poll_id].calculate_results()

    def resolve_tiebreak(self, poll_id: str):
        if poll_id not in self.polls or self.polls[poll_id].active:
            raise ValueError("La encuesta aún está activa.")

        poll = self.polls[poll_id]
        return self.tiebreaker_strategy.resolve_tiebreak(poll.options)


    def close_poll(self, poll_id: str):
        if poll_id in self.polls:
            self.polls[poll_id].close_poll()
            self.poll_repository.save_poll(self.polls[poll_id])
            # Notificar a los observadores cuando la encuesta se cierra
            self.notify_observers("poll_closed", {"poll_id": poll_id})
        else:
            raise ValueError("Encuesta no encontrada.")

