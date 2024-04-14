from unreliable_car import UnreliableCar
def test_unreliable_car():
        # Create an unreliable car with 50% reliability and 100 units of fuel
        unreliable_car = UnreliableCar("Rusty", 100, 50)

        # Drive the unreliable car for 50 units
        distance = unreliable_car.drive(50)
        print(f"Unreliable car drove {distance} units")
        print(unreliable_car)

        # Drive the unreliable car for another 100 units (more than the remaining fuel)
        distance = unreliable_car.drive(100)
        print(f"Unreliable car drove {distance} units")
        print(unreliable_car)


test_unreliable_car()