import cv2

winName = 'Faces'
cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_AUTOSIZE, cv2.WINDOW_AUTOSIZE)

carregaFace = cv2.CascadeClassifier("OpenCv\\cascade\\haarcascade_frontalface_alt.xml")
carregaEye = cv2.CascadeClassifier("OpenCv\\cascade\\haarcascade_eye.xml")

minhafoto = "fotos\\img2.jpg"
outro = "OpenCVScript\\fotos\\imagem4.jpg"
image = cv2.imread(outro)

grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = carregaFace.detectMultiScale(grayimage)

print(faces)

for (x, y, l, a) in faces:
    #arq, location, tamanho, color, espessura
    detect = cv2.rectangle(image, (x, y), (x+l, y+a), (0, 255, 0), 2)
    localEye = detect[y:y+a, x:x+l]
    localEyeGray = cv2.cvtColor(localEye, cv2.COLOR_HSV2RGB)
    detected = carregaEye.detectMultiScale(localEyeGray)

    for (ox, oy, ol, oa) in detected:
        localEye = cv2.rectangle(localEye, (ox, oy), (ox+ol, oy+oa), (255, 0, 0), 2)

cv2.imshow(winName, image)

if (cv2.waitKey(0)) :
    cv2.destroyAllWindows()