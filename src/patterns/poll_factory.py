from src.models.poll import Poll
from src.models.poll_multiple import PollMultiple
from src.models.poll_weighted import PollWeighted

class PollFactory:
    @staticmethod
    def create_poll(poll_id: str, question: str, options: list, duration: int, poll_type="simple"):
        if poll_type == "multiple":
            return PollMultiple(poll_id, question, options, duration)
        elif poll_type == "weighted":
            return PollWeighted(poll_id, question, options, duration)
        else:
            return Poll(poll_id, question, options, duration)
