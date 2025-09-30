from abc import ABC, abstractmethod

class BaseClient(ABC):
    @abstractmethod
    def __init__(self, model: str):
        pass
    