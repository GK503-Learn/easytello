from easytello import tello
import time
drone = tello.Tello()
drone.takeoff()
time.sleep(2)
drone.forward(30)
drone.land()
drone.takeoff()
drone.back(30)
