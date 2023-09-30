
from abc import ABC, abstractmethod

class AbstractTransformData(ABC):
    @abstractmethod
    def transform(self):
        pass