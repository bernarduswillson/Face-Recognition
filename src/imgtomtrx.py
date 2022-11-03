import cv2
import matplotlib.image as image
 
# Load the input image
image = cv2.imread(r'D:\Algeo02-21021\src\Untitled.jpg')
image = cv2.resize(image,(30, 30), interpolation = cv2.INTER_AREA)
cv2.imshow('Original', image)
cv2.waitKey(0)

# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0) 
 
# Window shown waits for any key pressing event

print('The Shape of the image is:',gray_image.shape)
print('The image as array is:')
print(gray_image[0:30,0:30])
a = input('Press any key to exit')

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0) 
 
# Window shown waits for any key pressing event
cv2.destroyAllWindows()
