import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True: 

    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 5000:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

            M = cv2.moments(contour)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame, "Red", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255), 3)
   

    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)   
    
    # Blue color
    low_blue = np.array([102, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    contours, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 5000:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

            M = cv2.moments(contour)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame, "Blue", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255), 3)
   
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Blue", blue)

    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 5000:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

            M = cv2.moments(contour)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame, "Green", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255), 3)
   

    cv2.imshow("Frame", frame)
    cv2.imshow("Green", green)

    # Yellow color
    low_yellow = np.array([15, 70, 120])
    high_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 5000:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

            M = cv2.moments(contour)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame, "Yellow", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255), 3)
   

    cv2.imshow("Frame", frame)
    cv2.imshow("Yellow", yellow)

    key = cv2.waitKey(1)
    if key == 27:
        break