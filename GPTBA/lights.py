class LightSwitch:
    def __init__(self, password):
        self.state = 0
        self.password = password

    def validate_password(self, entered_password):
        return entered_password == self.password

    def turn_on(self, entered_password):
        if self.validate_password(entered_password):
            self.state = 1
            print("The light switch is now on.")
        else:
            print("Incorrect password! Access denied.")

    def turn_off(self, entered_password):
        if self.validate_password(entered_password):
            self.state = 0
            print("The light switch is now off.")
        else:
            print("Incorrect password! Access denied.")

class Room:
    def __init__(self):
        self.light_switch = LightSwitch(1234)  # Create a LightSwitch object with password

    def switch_on_light(self, password):
        self.light_switch.turn_on(password)

    def switch_off_light(self, password):
        self.light_switch.turn_off(password)

# Example Usage
my_room = Room()
password = int(input("Please enter the password to turn on the light: "))
my_room.switch_on_light(password)
password = int(input("Please enter the password to turn off the light: "))
my_room.switch_off_light(password)
