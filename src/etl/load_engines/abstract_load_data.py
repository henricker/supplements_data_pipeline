from abc import ABC, abstractmethod

class AbstractLoadData(ABC):
    @abstractmethod
    def load(self):
        pass

