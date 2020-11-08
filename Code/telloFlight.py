# import easyTello API
from easyTello.easytello import tello
# import custom action functions
from telloFunctions import *

# initialize drone object
# drone = tello.Tello()
# while True, keep accepting user input for Tello commands
drone_in_flight = True

# UI: Allow user to see custom command and other selections
print('Tello User Interface\nEnter Tello commands listed in SDK 2.0\nAdditional Functions:\n1. Exit\n2. square-dance\n3. go-to-m1')

while(drone_in_flight):
    user_command = input('Enter a command: ')
    # end condition
    if(user_command == 'exit'):
        drone.land()
        drone.close()
        drone_in_flight = False
    elif(user_command == 'square-dance'):
        squareDance()
    elif(user_command == 'go-to-m1'):
        goToM1()
    elif(user_command == 'make-circle'):
        makeCircle()
    # SDK command
    else:
        drone.send_command(user_command, True)
