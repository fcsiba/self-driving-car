import picamera
import time

camera= picamera.PiCamera()
camera.vflip = True
camera.hflip = True
#raspivid -o -vf vid.h264
#raspivid -t 10000 -w 1920 -h 1080 -fps 25 -b 1200000 -p 0,0,1920,1080 -o pivideo.h264
#camera.capture('data/test1.jpg')
#camera.start_preview()
#camera.start_recording('/home/pi/Desktop/rec2.h264')
#time.sleep(5)
#camera.stop_recording
#camera.stop_preview()
#raspivid -o - -t 0 -hf -w 800 -h 400 -fps 24| cvlc -vvv stream:///dev/stdin --sout 'standard{access=http,mux=ts,dst=:8160}':demux=h264

camera.start_preview()
camera.start_recording('/home/pi/Desktop/data/testrun2.h264')
time.sleep(10)
camera.stop_recording()
camera.stop_preview()