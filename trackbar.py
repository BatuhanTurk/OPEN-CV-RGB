import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("Window")

cv2.createTrackbar("R","Window",0,255,nothing)
cv2.createTrackbar("G","Window",0,255,nothing)
cv2.createTrackbar("B","Window",0,255,nothing)
cv2.createTrackbar("ON / OFF","Window",0,1,nothing)

while(True):
    cv2.imshow("Window",img)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break
    r = cv2.getTrackbarPos("R","Window")
    g = cv2.getTrackbarPos("G","Window")
    b = cv2.getTrackbarPos("B","Window")
    s = cv2.getTrackbarPos("ON / OFF","Window")
    if(s == 1):
        img[:] = [0,0,0]
    else:
        img[:] = [b,g,r]
    
cv2.destroyAllWindows()