class LightBulb:
    def __init__(self):
        self.isOn = False

    def turn_on(self):
        self.isOn = True
        print("The light bulb is now on.")

    def turn_off(self):
        self.isOn = False
        print("The light bulb is now off.")

bulb = LightBulb()
command = ""
while command.lower() != "exit":
    command = input("Enter a command (turnon, turnoff, exit): ")

    if command.lower() == "turnon":
        bulb.turn_on()
    elif command.lower() == "turnoff":
        bulb.turn_off()
    elif command.lower() == "exit":
        print("Exiting program.")
    else:
        print("Invalid command. Please try again.")
