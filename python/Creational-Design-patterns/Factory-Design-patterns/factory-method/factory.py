from abc import ABC, abstractmethod
from notification import Noitification


class NotificationFactory(ABC):
    @abstractmethod
    def create(self) -> Noitification:
        pass