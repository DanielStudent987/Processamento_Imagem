from PIL import ImageGrab
from ultralytics import YOLO

import numpy as np
import cv2

while (True):
    img = ImageGrab.grab(bbox=(300,100, 800,800))

    frame = np.array(img)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    model = YOLO("yolov8n.pt")

    result = model.predict(source=img)
    print(result)
    #for detect in result:
        