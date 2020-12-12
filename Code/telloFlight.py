# import easyTello API
from easyTello.easytello import tello
# import custom action functions
from telloFunctions import *

# while True, keep accepting user input for Tello commands
drone_in_flight = True

# UI: Allow user to see custom command and other selections
print('Tello User Interface\nEnter Tello commands listed in SDK 2.0\nAdditional Functions:\n1. Exit\n2. square-dance\n3. go-to-m1(-m8)\n4. make-circle')

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
    elif(user_command == 'go-to-m2'):
        goToM2()
    elif(user_command == 'go-to-m3'):
        goToM3()
    elif(user_command == 'go-to-m4'):
        goToM4()
    elif(user_command == 'go-to-m5'):
        goToM5()
    elif(user_command == 'go-to-m6'):
        goToM6()
    elif(user_command == 'go-to-m7'):
        goToM7()
    elif(user_command == 'go-to-m8'):
        goToM8()
    elif(user_command == 'route-to-m1'):
        routeToM1()
    elif(user_command == 'make-circle'):
        makeCircle()
    elif(user_command == 'trial'):
        trial()
    # SDK command
    else:
        drone.send_command(user_command, True)
