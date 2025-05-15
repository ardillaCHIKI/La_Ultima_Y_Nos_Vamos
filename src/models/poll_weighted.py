# src/models/poll_weighted.py
from src.models.poll import Poll

class PollWeighted(Poll):
    def __init__(self, poll_id: str, question: str, options: list, duration: int):
        super().__init__(poll_id, question, options, duration)
        self.user_votes = {}

    def vote(self, user_id: str, option: str, weight: int):
        if self.active and option in self.options and weight > 0:
            self.user_votes[user_id] = (option, weight)
            self.options[option] += weight
        else:
            raise ValueError("Encuesta cerrada, opción inválida o peso inválido.")

