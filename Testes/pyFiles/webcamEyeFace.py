import cv2

winName = 'Faces'
cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_AUTOSIZE, cv2.WINDOW_AUTOSIZE)

carregaCam = cv2.CascadeClassifier("OpenCVScript\\Haarcascade\\haarcascade_frontalface_alt.xml")
carregaEye = cv2.CascadeClassifier("OpenCVScript\\Haarcascade\\haarcascade_eye.xml")

video = cv2.VideoCapture(0)



while (True):

    conec, frame = video.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = carregaCam.detectMultiScale(grayframe, scaleFactor=1.08)


    for (x, y, l, a) in faces:
        cv2.rectangle(frame, (x,y), (x+l, y+a), (0, 255, 0), 2)

        localEye = frame[ y:y+a, x:x+l]
        grayeye = cv2.cvtColor(localEye, cv2.COLOR_BGR2GRAY)
        eyes = carregaEye.detectMultiScale(grayeye,  scaleFactor=1.08, minNeighbors=4)

        for (ox, oy, ol, oa) in eyes:
            detectEye = cv2.rectangle(localEye, (ox, oy), (ox+ol, oy+oa), (255, 0 ,0), 2)
            cv2.circle(localEye, (int(ox+(ol/2)), int(oy+(oa/2))), 5, (0, 0 ,255), 2)






    k = cv2.waitKey(1)
    if (k == ord('q')) :
        break

    cv2.imshow(winName, frame)
    

video.release()
cv2.destroyAllWindows()