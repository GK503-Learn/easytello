import cv2
from easytello import tello

drone = tello.Tello()
drone.takeoff()
drone.streamon()

cap = cv2.VideoCapture("") # fill this out with the ip addr of video stream fom tello

while True:
    # ret is a boolean that holds if openCV got a frame or not, frame just holds the data for the frame captured
    ret, frame = cap.read()
    
    if ret:
        cv2.imshow("Tello", frame)
        
    # if cv2.waitKey(1) and 0xFF == ord("q"):
       # break;

cap.release()
cv2.destroyAllWindows()
drone.streamoff()
drone.land()