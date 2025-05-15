# patterns/strategy.py

import json
import random

class TieBreakerStrategy:
    def resolve_tiebreak(self, votes: dict):
        pass

class AlphabeticalTieBreaker(TieBreakerStrategy):
    def resolve_tiebreak(self, votes: dict):
        return sorted(votes.keys())[0]

class RandomTieBreaker(TieBreakerStrategy):
    def resolve_tiebreak(self, votes: dict):
        return random.choice(list(votes.keys()))

class ResultFormatStrategy:
    def format_results(self, votes: dict):
        pass

class TextResultFormat(ResultFormatStrategy):
    def format_results(self, votes: dict):
        return str(votes)

class JSONResultFormat(ResultFormatStrategy):
    def format_results(self, votes: dict):
        return json.dumps(votes, indent=4)
