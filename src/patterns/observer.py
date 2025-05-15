
class Observer:
    def update(self, event: str, data: dict):
        pass

class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, event: str, data: dict):
        for observer in self.observers:
            observer.update(event, data)
