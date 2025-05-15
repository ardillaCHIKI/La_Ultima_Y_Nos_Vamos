# src/models/vote.py
class Vote:
    def __init__(self, user_id: str, poll_id: str, option: str):
        self.user_id = user_id
        self.poll_id = poll_id
        self.option = option
