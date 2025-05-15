# src/models/poll.py
from datetime import datetime

class Poll:
    def __init__(self, poll_id: str, question: str, options: list, duration: int):
        self.poll_id = poll_id
        self.question = question
        self.options = {option: 0 for option in options}
        self.start_time = datetime.now()
        self.end_time = self.start_time.timestamp() + duration
        self.active = True

    def vote(self, user_id: str, option: str):
        if self.active and option in self.options:
            self.options[option] += 1
        else:
            raise ValueError("La encuesta está cerrada o la opción no es válida.")

    def close_poll(self):
        self.active = False
