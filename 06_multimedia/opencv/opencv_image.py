import cv2

img = cv2.imread('se7en.jpeg')
img2 = cv2.resize(img, (1000, 700))

edge = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('IMG', img)
cv2.imshow('Edge 1', edge)
cv2.imshow('Edge 2', edge2)
cv2.imshow('Edge 3', edge3)

cv2.waitKey(0)

cv2.destroyAllWindows()