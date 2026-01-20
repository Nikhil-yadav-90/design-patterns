from product_interface import Chair, Sofa
from abc import ABC, abstractmethod



class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair()->Chair:
        pass

    @abstractmethod
    def create_sofa()->Sofa:
        pass

