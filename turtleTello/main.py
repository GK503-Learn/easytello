def make_a_square(drone, side_length):
    for i in  range(4):
        drone.forward(side_length)
        drone.cw(90)

from turtleTello import tello

drone = tello.Tello()

drone.takeoff()
make_a_square(drone, 20)
drone.land()