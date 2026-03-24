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

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


h = Elevator(1, 10)

h.go_to_floor(5)
print(f"Current Floor: {h.current_floor}")

h.go_to_floor(1)
print(f"Current Floor: {h.current_floor}")

building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.run_elevator(2, 3)

building.fire_alarm()