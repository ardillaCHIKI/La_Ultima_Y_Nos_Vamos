import pytest
from src.patterns.observer import Subject, Observer
from src.patterns.factory import PollFactory
from src.models.poll_multiple import PollMultiple
from src.patterns.strategy import AlphabeticalTieBreaker, RandomTieBreaker

class MockObserver(Observer):
    def __init__(self):
        self.updated = False

    def update(self, event, data):
        self.updated = True

def test_observer_pattern():
    subject = Subject()
    observer = MockObserver()
    subject.add_observer(observer)
    subject.notify_observers("poll_closed", {})
    assert observer.updated == True

def test_factory_pattern():
    poll = PollFactory.create_poll("1", "¿Mejor juego?", ["Minecraft", "Zelda"], 60, "multiple")
    assert isinstance(poll, PollMultiple)

def test_strategy_pattern():
    votes = {"A": 3, "B": 3}
    assert AlphabeticalTieBreaker().resolve_tiebreak(votes) == "A"
    assert RandomTieBreaker().resolve_tiebreak(votes) in ["A", "B"]
