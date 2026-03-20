class Car:

    current_speed = 0
    travelled_distance = 0

    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed

car = Car("ABC-123", 142)

print(f"License plate: {car.license_plate}\nMaximum speed: {car.maximum_speed} km/h\nCurrent speed: {car.current_speed} km/h\nTravelled distance: {car.travelled_distance} km")

