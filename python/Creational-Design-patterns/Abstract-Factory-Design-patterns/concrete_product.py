from product_interface import Chair, Sofa


class VictorianSofa(Sofa):
    def lie_on(self):
        print("I am lie on victorian sofa")

class VictorianChair(Chair):
    def sit_on(self):
        print("I am sitting on victorian chair")

class ModernSofa(Sofa):
    def lie_on(self):
        print("I am lie on modern sofa")

class ModernChair(Chair):
    def sit_on(self):
        print("I am sitting on modern chair")