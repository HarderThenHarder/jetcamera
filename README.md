## jetcamera
---
This is a pakage which can easily use USB & CSI camera on jetson.<br><br>

### Setup
```python
sudo python3 setup.py install
```

### Usage
```python
# CSI Camera
from jetcamera.camera import CSICamera
camera = CSICamera()
frame = camera.read()

# USB Camera
from jetcamera.camera import USBCamera
camera = USBCamera(0)   # USB-Camera's index, chech it in /dev/video*
frame = camera.read()
```
