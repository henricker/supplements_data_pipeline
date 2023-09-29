from abc import ABC, abstractmethod

class AbstractExtractWebsite(ABC):
    @abstractmethod
    def extract(self):
        pass