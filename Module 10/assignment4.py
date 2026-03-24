import random

# Car class ---------------------------------------------------
class Car:

    current_speed = 0
    travelled_distance = 0

    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed

    # Acceleration
    def accelerate(self, accelerate):

        if accelerate + self.current_speed < self.maximum_speed:
            self.current_speed += accelerate
            if self.current_speed < 0:
                self.current_speed = 0
        else:
            self.current_speed = self.maximum_speed

    # Distance
    def drive(self, hours):
        self.travelled_distance += int(hours * self.current_speed)

    def __str__(self):
        return f"{self.license_plate} | Speed: {self.current_speed} km/h | Distance: {self.travelled_distance} km"

# Race class ---------------------------------------------------
class Race:

    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(f"{car.license_plate:<12} | {car.maximum_speed:<10} | {car.current_speed:<15} | {car.travelled_distance:<10}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True

        return False


cars = []
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)
print(f"Race created: {race.name} ({race.distance} km)")
print(f"Cars participating: {len(race.cars)}")

# Test
for hour in range(100):
    race.hour_passes()
    if race.race_finished():
        break

print(f"\nRace finished initially: {race.race_finished()}")
race.print_status()