import cv2

# xml 분류기 필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
img = cv2.imread('Avergers.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이미지에서 얼굴 식별
faces = face_cascade.detectMultiScale(gray)


# p1 (x, y)
# p2 (x + w, y + h)
#(255, 0, 0) BGR -> 파란색
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)  

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()