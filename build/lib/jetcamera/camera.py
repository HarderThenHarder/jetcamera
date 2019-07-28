import cv2


class CSICamera():
    def __init__(self, capture_width=1280, capture_height=720, display_width=1280, display_height=720, fps=30, flip_method=2):
        try:
            self.cap = cv2.VideoCapture(self.gstreamer_pipeline(capture_width, capture_height, display_width, display_height, fps, flip_method), cv2.CAP_GSTREAMER)
        except:
            raise IOError("Couldn't Find CSI-Camera.")

    def gstreamer_pipeline (self, capture_width, capture_height, display_width, display_height, framerate, flip_method) :   
        return ('nvarguscamerasrc ! ' 
        'video/x-raw(memory:NVMM), '
        'width=(int)%d, height=(int)%d, '
        'format=(string)NV12, framerate=(fraction)%d/1 ! '
        'nvvidconv flip-method=%d ! '
        'video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! '
        'videoconvert ! '
        'video/x-raw, format=(string)BGR ! appsink'  % (capture_width,capture_height,framerate,flip_method,display_width,display_height))

    def read(self):
        ret, image = self.cap.read()
        if ret:
            return image
        else:
            raise RuntimeError("Camera Lost.")

class USBCamera():
    def __init__(self, camera_idx, capture_width=640, capture_height=480, fps=30):
        self.cap = cv2.VideoCapture(camera_idx)
        if not self.cap.isOpened():
            raise IOError("Couldn't Find USB-Camera.")
        self.cap.set(3, capture_width)
        self.cap.set(4, capture_height)
        self.cap.set(5, fps)

    def read(self):
        ret, image = self.cap.read()
        if ret:
            return image
        else:
            raise RuntimeError("Camera Lost.")
