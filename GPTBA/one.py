class One:
    def __init__(self, value=0):
        self.color = "red"
        self.value = value

    def change_color(self, value):
        self.value = value
        if self.value == 2:
            self.color = "blue"
            print("The color is now blue.")
        else:
            self.color = "red"
            print("The color is now red.")

class Board:
    def __init__(self):
        self.one_object = One()

    def get_input(self):
        while True:  # Infinite loop
            user_input = input("Enter a number (1 for red, 2 for blue) or 'exit' to quit: ")
            if user_input.lower() == 'exit':  # Check for exit command
                print("Exiting program.")
                break
            try:
                value = int(user_input)
                self.one_object.change_color(value)
            except ValueError:
                print("Invalid input! Please enter 1, 2, or 'exit'.")

# Example usage:
board_instance = Board()
board_instance.get_input()
