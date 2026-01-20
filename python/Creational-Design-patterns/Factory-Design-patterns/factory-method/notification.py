from abc import abstractmethod, ABC


class Noitification(ABC):
    @abstractmethod
    def notify(self, message):
        pass