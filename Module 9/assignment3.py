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

car = Car("ABC-123", 142)
print(f"Initial distance: {car.travelled_distance} km")
car.current_speed = 60
car.drive(1.5)
print(f"Distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")