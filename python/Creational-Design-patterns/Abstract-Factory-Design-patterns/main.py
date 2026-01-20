from concrete_factories import VictorianFurniture, ModernFurniture


if __name__ == "__main__":
    factory = VictorianFurniture()
    chair = factory.create_chair()
    chair.sit_on()
    sofa = factory.create_sofa()
    sofa.lie_on()
    