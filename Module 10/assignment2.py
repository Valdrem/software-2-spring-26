class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, desired_floor):

        # Current floor before while loop
        print(f"The elevator is at floor: {self.current_floor}")

        while self.current_floor < desired_floor:
            self.floor_up()
        while self.current_floor > desired_floor:
            self.floor_down()

    def floor_up(self):
        self.current_floor += 1
        print(f"The elevator is at floor: {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"The elevator is at floor: {self.current_floor}")


class Building:

    def __init__(self, bottom_floor, top_floor, elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for e in range(elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)

    def run_elevator(self, elevator_number, destination_floor):
        target_elevator = self.elevators[elevator_number]
        target_elevator.go_to_floor(destination_floor)


h = Elevator(1, 10)

h.go_to_floor(5)
print(f"Current Floor: {h.current_floor}")

h.go_to_floor(1)
print(f"Current Floor: {h.current_floor}")

# Test Building with multiple elevators
building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 3)
building.run_elevator(2, 8)

# Test single elevator building
small_building = Building(0, 5, 1)
small_building.run_elevator(0, 4)

# Test larger building
office = Building(1, 6, 5)
office.run_elevator(0, 4)
office.run_elevator(4, 2)