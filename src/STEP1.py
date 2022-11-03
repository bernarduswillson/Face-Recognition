import cv2
import matplotlib.image as image

def ImgToMtrx(img):
    image = cv2.imread(r'img')
    image = cv2.resize(image,(4,4), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = gray_image.flatten()
    return result

