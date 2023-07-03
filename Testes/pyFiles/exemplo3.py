import cv2
import numpy as np

arq = str(input("Nome do arquivo: "))
image = cv2.imread(arq)



altura, largura, pxl = np.shape(image)

for py in range(0, altura):
    for px in range(0,largura):
        if (py%2==1 and px%2==1) :
            image[py, px] = (0, 0, 255)
            #print(image[py,px])

image[10:50, 10:50] = (255, 0 , 255)

cv2.imshow("Original", image)


k = cv2.waitKey(0)

if (k==ord('q')) :
    cv2.destroyAllWindows()

