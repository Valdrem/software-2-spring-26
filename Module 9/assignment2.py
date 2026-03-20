class Car:

    current_speed = 0
    travelled_distance = 0

    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed

    def accelerate(self, acceleration):

        if acceleration + self.current_speed < self.maximum_speed:
            self.current_speed += acceleration
            if self.current_speed < 0:
                self.current_speed = 0
        else:
            self.current_speed = self.maximum_speed


car = Car("ABC-123", 142)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current speed: {car.current_speed} km/h")
car.accelerate(-200)
print(f"Current speed: {car.current_speed} km/h")

