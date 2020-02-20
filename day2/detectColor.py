import numpy as np
import cv2

#webcamera no 0 is used to store frames
cap = cv2.VideoCapture(0)
cap.set(3,320) # set Width
cap.set(4,240) # set Height

while(1):
    #capture live streams frame-by-frame
    ret,frame = cap.read()

    #converts image from BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    print hsv
    
    lower_red = np.array([110,50,50])
    upper_red = np.array([130,250,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cv2.destroyAllWindows()
cap.release()
