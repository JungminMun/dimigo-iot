import cv2

# xml 분류기 필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

img = cv2.imread('Avergers.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이미지에서 얼굴 식별
faces = face_cascade.detectMultiScale(gray)

# p1 (x, y)
# p2 (x + w, y + h)
#(255, 0, 0) BGR -> 파란색
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)  

    # 얼굴이 검출된 영역 내부
    # ROI
    roi_color = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]

    # 눈 식별
    eyes = eye_cascade.detectMultiScale(roi_gray)

    #for문 돌리기
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ex + eh), (0, 255, 0), 2)


cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()