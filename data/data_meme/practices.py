import cv2

img = cv2.imread('bg.pn', 1)
img = cv2.resize(img, (500, 180))

cv2.imwrite('bg.png', img)




