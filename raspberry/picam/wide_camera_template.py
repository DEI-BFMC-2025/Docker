from libcamera import Transform
from picamera2 import Picamera2,Preview
import time
picam2=Picamera2()
#mode 2 of V3 camera should be uncropped and full resolution (I think!)
mode = picam2.sensor_modes[0]
q_w=mode['size'][0]//4
q_h=mode['size'][1]//4

print (q_w,q_h)

picam2.start_preview(Preview.QTGL,x=100,y=100,width=q_w,height=q_h)
quarter=(q_w,q_h)
q_size=tuple(quarter)

config = picam2.create_still_configuration(transform=Transform(hflip=1,vflip=1),
                                           sensor={'output_size': mode['size'],'bit_depth':mode['bit_depth']},
                                           lores={'size':q_size}, display='lores')
picam2.configure(config)
picam2.start()
time.sleep(100)
#picam2.capture_file('Uncropped.jpg')

picam2.stop()
