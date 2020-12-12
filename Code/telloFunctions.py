# Author: Christian Caldwell
# import easyTello API
from easyTello.easytello import tello

# initialize drone object
drone = tello.Tello()

def squareDance():
    drone.takeoff()
    for i in range(4):
        drone.forward(100)
        drone.flip('f')
        drone.cw(90)
    drone.land()

def makeCircle():
    drone.takeoff()
    drone.curve(70,70,0,140,0,0,60)
    drone.cw(180)
    drone.curve(70,70,0,140,0,0,60)
    drone.land()

# misson pad functions
def goToM1():
    drone.takeoff()
    drone.mon()
    drone.go(100, 100, 100, 60, 'm1')
    drone.land()

def goToM2():
    drone.takeoff()
    drone.mon()
    drone.go(100, 100, 100, 60, 'm2')
    drone.land()

def goToM3():
    drone.takeoff()
    drone.mon()
    drone.go(100, 100, 100, 60, 'm3')
    drone.land()

def goToM4():
    drone.takeoff()
    drone.mon()
    drone.go(100, 100, 100, 60, 'm4')
    drone.land()

def goToM5():
    drone.takeoff()
    drone.mon()
    drone.go(100, 100, 100, 60, 'm5')
    drone.land()

def goToM6():
    drone.takeoff()
    drone.mon()
    drone.go(100, 100, 100, 60, 'm6')
    drone.land()

def goToM7():
    drone.takeoff()
    drone.mon()
    drone.go(100, 100, 100, 60, 'm7')
    drone.land()

def goToM8():
    drone.takeoff()
    drone.mon()
    drone.go(100, 100, 100, 60, 'm8')
    drone.land()

def routeToM1():
    drone.takeoff()
    #drone.up(200)
    drone.go(0,0,0,40,'m1')
    drone.land()

def trial():
    drone.takeoff()
    drone.up(300)
    drone.forward(200)
    drone.cw(180)
    drone.flip('f')
    drone.forward(150)
    drone.land()
    
