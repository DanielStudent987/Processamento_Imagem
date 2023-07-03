import cv2
from ultralytics import YOLO

video = cv2.VideoCapture(0)

while (True) :

    conec, frame = video.read()

    cv2.imshow("Video",frame)

    k = cv2.waitKey(1)
    if (k == ord('q')) :
        break

video.release()
cv2.destroyAllWindows()