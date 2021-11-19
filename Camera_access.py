import cv2
import numpy as np

# returns video from the first webcam
cap = cv2.VideoCapture(0)

while True:
    # ret is a boolean variable that returns true if the frame is available.
    # cap.read() returns a bool. If frame is read correctly, it returns True.
    ret, frame = cap.read()
    
    # displays a frame in a window
    cv2.imshow('frame',frame)
    
    # cv2.waitkey(1) returns a 32-bit integer corresponding to the pressed key
    # 0xFF sets the left 24 bits to zero
    # ord('q') returns the ASCII value of q
    # Thus, we check if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# releases the webcam.
cap.release()

# closes all of the imshow() windows.
cv2.destroyAllWindows()

