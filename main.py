def make_a_square(drone, side_length):
    for i in  range(4):
        drone.forward(side_length)
        drone.cw(90)


from easytello import tello

drone = tello.Tello()
drone.takeoff()
make_a_square(drone, 20)
drone.land()
# help(drone)

# drone.forward()
# drone.back()
# drone.ccw()
# drone.cw()
# drone.up()
# drone.go()