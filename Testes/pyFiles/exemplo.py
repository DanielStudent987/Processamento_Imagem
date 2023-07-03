import cv2
video = cv2.VideoCapture(0)

img = cv2.imread('sintique2019.jpg')

cv2.imshow('image', img)

k = cv2.waitKey(0)
print(k)

if (k==ord('q')):
    
    cv2.destroyAllWindows()
    

while(True):
    """
    conectado, frame = video.read()

    cv2.imshow("Video", frame)
    
    
    if (cv2.waitKey(0)=='q'):
        break
    """
    break

#video.release()
#cv2.destroyAllWindows()
    
    
