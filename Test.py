import cv2
import numpy as np

cap=cv2.VideoCapture(1)

def doNothing(x):
    pass


while True:
    ret, img=cap.read()

    myhsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_r=np.array([170,50,50])
    u_r=np.array([200,255,255])
    mymask=cv2.inRange(myhsv,l_r,u_r)
    result=cv2.bitwise_and(img,img,mask=mymask)

    cv2.imshow("Normal Video", img)
    cv2.imshow("Color detection",result)

    k=cv2.waitKey(100)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
