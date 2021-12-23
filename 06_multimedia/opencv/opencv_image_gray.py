import cv2

img = cv2.imread('se7en.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('se7en', img)
cv2.imshow('se7en gray', gray)

while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('se7en_gray.jpg')

cv2.waitKey(0)

cv2.destroyAllWindows()