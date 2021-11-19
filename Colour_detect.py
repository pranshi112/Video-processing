import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True: 

    ret, frame = cap.read()
    
    # to reduce noise in images, image smoothing is done using cv2.GaussianBlur
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    
    # converting frame to HSV format
    # cv2.COLOR_BGR2HSV converts from default BGR format to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    
    # passing the lowest HSV values of red
    low_red = np.array([161, 155, 84])
    
    # passing the highest HSV values of red
    high_red = np.array([179, 255, 255])
    
    # we use this mask on hsv_frame with values in the passed range
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    # Using only red_mask shows red color in white but using this line, we see red in red
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # first argument in cv2.findContours() is source image, second is contour retrieval mode, third is contour approximation method
    # cv2.RETR_TREE retrieves all possible contours from the image
    # cv2.CHAIN_APPROX_NONE stores all the points on the boundary(i.e. stores edges) and not just vertices
    # contours here is a list of all the contours in the image
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    # finding area for each contour
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 5000:
            # first argument is source image, second is the contours from the list, third is index of contours(to draw all contours, pass -1)
            # remaining arguments are color, thickness
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

            # Image moments help to calculate the centroid of the image
            M = cv2.moments(contour)

            # Calculating centroids
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            # finding center by drawing a circle at the center
            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            
            # putting text of the detected color
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
    # 27 is ASCII code for Esc key
    if key == 27:
        break
