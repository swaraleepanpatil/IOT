import cv2
cap = cv2.VideoCapture(1)
while(True):
    #capture frame-by-frame
    ret,frame = cap.read()

    #display resulting frame
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
#when everything done, release capure
cap.release()
cv2.destroyAllWindows()

