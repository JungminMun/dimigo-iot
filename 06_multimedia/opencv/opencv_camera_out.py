import cv2

# 카메라 장치를 열기
cap = cv2.VideoCapture(0) #카메라 디바이스 번호

if not cap.isOpened():
    print('Camera Open Failed')
    exit()


# DIVX (avi), MP4V(mp4), X264(h264), 
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))

#동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    out.write(frame)

    # 1000-> 1초 10 -> 0.01초
    if cv2.waitKey(10) == 13:
        break

cap.release()
out.release()
cv2.destroyAllWindows()