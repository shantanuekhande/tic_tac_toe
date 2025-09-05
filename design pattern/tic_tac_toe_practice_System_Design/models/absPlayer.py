from abc import ABC, abstractmethod
class AbsPlayer(ABC):
    @abstractmethod
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol