import picamera
import time

path = '/home/pi/src6/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)

    while True:
        cmd = input('photo : 1, video : 2, exit : 9 ')

        nowTime = time.strftime("%y%m%d_%H%M%S")

        if cmd == '1':
            camera.capture('%s/%sphoto.jpg' %(path,nowTime))
            print('사진 촬영')
        elif cmd == '2':
            camera.start_recording('%s/%svideo.h264' %(path,nowTime))
            input('press enter to stop')
            camera.stop_recording()
            print('동영상 촬영')
        elif cmd == '9':
            break
        else:
            print('incorrect command')

finally:
    camera.stop_preview()