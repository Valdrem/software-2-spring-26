import random

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

    # Add this method to print cars nicely
    def __str__(self):
        return f"{self.license_plate} | Speed: {self.current_speed} km/h | Distance: {self.travelled_distance} km"

# Cars list
cars = [
    Car("ABC - 123", 200),
    Car("DEF - 456", 200),
    Car("HIJ - 789", 200),
    Car("KLM - 012", 200)
]

# Race
def race(cars):

    race_finished = False
    while not race_finished:
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1.0)
            if car.travelled_distance >= 10000:
                race_finished = True
    return cars

race(cars)

for car in cars:
    print(car)

