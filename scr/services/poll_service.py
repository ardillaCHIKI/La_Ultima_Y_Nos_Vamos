from models.poll import Poll
from repositories.poll_repository import PollRepository
from datetime import datetime

class PollService:
    def __init__(self, poll_repository: PollRepository):
        self.poll_repository = poll_repository
        self.polls = {}

    def create_poll(self, poll_id: str, question: str, options: list, duration: int):
        poll = Poll(poll_id, question, options, duration)
        self.polls[poll_id] = poll
        self.poll_repository.save_poll(poll)

    def vote(self, user_id: str, poll_id: str, option: str):
        if poll_id in self.polls:
            self.polls[poll_id].vote(user_id, option)
            self.poll_repository.save_poll(self.polls[poll_id])
        else:
            raise ValueError("Encuesta no encontrada.")

    def close_poll(self, poll_id: str):
        if poll_id in self.polls:
            self.polls[poll_id].close_poll()
            self.poll_repository.save_poll(self.polls[poll_id])
        else:
            raise ValueError("Encuesta no encontrada.")
