import cv2
import numpy as np
import time
import Controller

lowerBound=np.array([105,122,0]) #pink detection
#lowerBound=np.array([0,193,42]) #orange detection
upperBound=np.array([180,255,255])

cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

while True:
    ret, img=cam.read()
    img=cv2.resize(img,(800,600))
    # img=cv2.resize(img,(340,220))

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    _, conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(img,conts,-1,(255,0,0),3)
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
        dumbbell = 2
        if(x > 400):
            dumbbell = 1
        Controller.playerinput(1, dumbbell, y)

    cv2.imshow("cam",img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        cam.release()
        cv2.destroyAllWindows()
        break
