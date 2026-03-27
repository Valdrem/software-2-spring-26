class Car:

    current_speed = 0
    travelled_distance = 0

    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed

    # Acceleration
    def accelerate(self, acceleration):

        if acceleration + self.current_speed < self.maximum_speed:
            self.current_speed += acceleration
            if self.current_speed < 0:
                self.current_speed = 0
        else:
            self.current_speed = self.maximum_speed

    # Distance
    def drive(self, hours):
        self.travelled_distance += int(hours * self.current_speed)


class ElectricCar(Car):

    def __init__(self, license_plate, maximum_speed, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(license_plate, maximum_speed)


class GasolineCar(Car):

    def __init__(self, license_plate, maximum_speed, tank_volume):
        self.tank_volume = tank_volume
        super().__init__(license_plate, maximum_speed)


# Test
car = Car("TEST-123", 150)
print(f"Car created: {car.license_plate}, max speed: {car.maximum_speed}")

electric = ElectricCar("ELEC-123", 200, 75.0)
print(f"Electric car: {electric.license_plate}, max speed: {electric.maximum_speed}, battery: {electric.battery_capacity} kWh")

gasoline = GasolineCar("GAS-123", 180, 50.0)
print(f"Gasoline car: {gasoline.license_plate}, max speed: {gasoline.maximum_speed}, tank: {gasoline.tank_volume} l")

electric.accelerate(100)
gasoline.accelerate(80)
print(f"After acceleration - Electric: {electric.current_speed} km/h, Gasoline: {gasoline.current_speed} km/h")

electric.drive(2)
gasoline.drive(2)
print(f"After 2 hours - Electric: {electric.travelled_distance} km, Gasoline: {gasoline.travelled_distance} km")