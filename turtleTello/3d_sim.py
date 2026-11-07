from tello_sim.patch import use_simulator
use_simulator()    # patches djitellopy to talk to the sim over UDP

from djitellopy import Tello
drone = Tello(host="127.0.0.1")
drone.connect()
drone.takeoff()
drone.move_forward(100)
drone.rotate_clockwise(90)
drone.land()