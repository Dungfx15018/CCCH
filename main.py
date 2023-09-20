import cv2
import time
import numpy as np
import hand as hd
import math

cap2 = cv2.VideoCapture(0)
pTime = 0


detector = hd.handDetector(detectionCon=0.7)


while True:
    res, frame = cap2.read()

    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame,draw = False)
    if len(lmList) !=0:

        x1, y1 = lmList[4][1], lmList[4][2] # toa do ngon dau
        x2, y2 = lmList[8][1], lmList[8][2] # toa do ngon cai


        cv2.circle(frame, (x1,y1), 15,(255,0,255), -1)
        cv2.circle(frame, (x2,y2), 15, (255,0,255), -1)
        cv2.line(frame, (x1,y1), (x2,y2), (255,0,255),3)

        cx,cy =  (x1+x2)//2, (y1+y2)//2
        cv2.circle(frame, (cx,cy), 15, (255,0,255), -1)
        length = math.hypot(x2-x1,y2-y1)
        print(length)

    cTime = time.time()
    fps = 1.0 /(cTime - pTime)
    pTime = cTime

    cv2.putText(frame, f"FPS: {int(fps)}", (150,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0),3)
    cv2.imshow("jun", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap2.release()
cv2.destroyAllWindows()