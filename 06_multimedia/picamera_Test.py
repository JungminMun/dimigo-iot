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

        if cmd == '1':
            camera.capture('%s/photo.jpg' %path)
        elif cmd == '2':
            camera.start_recording('%s/video.h264' % path)
            input('press enter to stop')
            camera.stop_recording()

finally:
    camera.stop_preview()