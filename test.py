from jetcamera.camera import CSICamera
from jetcamera.camera import USBCamera
import cv2

camera = CSICamera(800, 400, 800, 400)
# camera = USBCamera(1)

while True:
    frame = camera.read()
    
    cv2.imshow("test", frame)
    if cv2.waitKey(1) == ord('q'):
        break