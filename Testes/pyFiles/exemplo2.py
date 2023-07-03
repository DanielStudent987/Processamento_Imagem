import argparse
import cv2

#import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

print ("width: {} pixels".format(image.shape[1]))
print ("height: {} pixels".format(image.shape[0]))
print ("channels: {}".format(image.shape[2]))


# extract contours from the image
#cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cnts = imutils.grab_contours(cnts)

# loop over the contours and draw them on the input image
#for c in cnts:
	#cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
# display the total number of shapes on the image
#text = "I found {} total shapes".format(len(cnts))
#cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
# write the output image to disk
cv2.imwrite(args["output"], image)

#cv2.imwrite("image", image)
'''
cv2.imshow("Image", image)

k = cv2.waitKey(0)

if (k==ord('q')) :
    cv2.destroyAllWindows()
    '''
