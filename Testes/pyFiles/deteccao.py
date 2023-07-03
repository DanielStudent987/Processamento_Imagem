import cv2

winName = 'Faces'
cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_AUTOSIZE, cv2.WINDOW_AUTOSIZE)

carrega = cv2.CascadeClassifier("OpenCv/cascade/haarcascade_frontalface_alt.xml")

image = cv2.imread("fotos\\img7.jpg")

grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = carrega.detectMultiScale(grayimage, scaleFactor=1.06, minNeighbors=3, minSize=(30, 30))

print(faces)

for (x, y, l, a) in faces:
    #arq, location, tamanho, color, espessura
    cv2.rectangle(image, (x, y), (x+l, y+a), (0, 255, 0), 2)

cv2.imshow(winName, image)

if (cv2.waitKey(0)) :
    cv2.destroyAllWindows()