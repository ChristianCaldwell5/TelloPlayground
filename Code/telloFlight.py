# import easyTello API
from easyTello.easytello import tello

# initialize drone object
drone = tello.Tello()
# while True, keep accepting user input for Tello commands
drone_in_flight = True

# UI: Allow user to see custom command and other selections
print('Tello User Interface\nEnter Tello commands listed in SDK 2.0\nAdditional Functions:\n1. Exit\n2. square-dance')

def squareDance():
    drone.takeoff()
    for i in range(4):
        drone.forward(100)
        drone.flip('f')
        drone.cw(90)
    drone.land()

while(drone_in_flight):
    user_command = input('Enter a command: ')
    # end condition
    if(user_command == 'exit'):
        drone.land()
        drone_in_flight = False
    elif(user_command == 'square-dance'):
        squareDance()
    else:
        drone.send_command(user_command, True)
