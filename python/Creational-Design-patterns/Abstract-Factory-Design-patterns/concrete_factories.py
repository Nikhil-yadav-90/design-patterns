from abstract_factory import FurnitureFactory
from concrete_product import VictorianChair, VictorianSofa, ModernChair, ModernSofa

class VictorianFurniture(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()
    def create_sofa(self):
        return VictorianSofa()

class ModernFurniture(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    def create_sofa(self):
        return ModernSofa()