from models.poll import Poll

class PollMultiple(Poll):
    def __init__(self, poll_id: str, question: str, options: list, duration: int):
        super().__init__(poll_id, question, options, duration)
        self.user_votes = {}

    def vote(self, user_id: str, selected_options: list):
        if self.active and all(option in self.options for option in selected_options):
            self.user_votes[user_id] = selected_options
            for option in selected_options:
                self.options[option] += 1
        else:
            raise ValueError("Encuesta cerrada o opciones inválidas.")
