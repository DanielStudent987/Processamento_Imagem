from PIL import ImageGrab
from ultralytics import YOLO

import torch
import numpy as np
import cv2

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while (True):

    img = ImageGrab.grab(bbox=(0, 0, 1000,700))

    frame = np.array(img)

    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    

    result = model(img)
    
    for detect in result:

        boxes = detect.boxes
        for box in boxes:
            x,y,w,h = box.xywh[0]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Frames", frame)

    if (cv2.waitKey(0)):
        break

cap.release()
cv2.destroyAllWindows()

        