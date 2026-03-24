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


h = Elevator(1, 10)

h.go_to_floor(5)
print(f"Current Floor: {h.current_floor}") # Should be 5

h.go_to_floor(1)
print(f"Current Floor: {h.current_floor}") # Should be 1