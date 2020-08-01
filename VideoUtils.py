import cv2

def get_frame(video, frame):
    video.set(cv2.CAP_PROP_POS_MSEC, frame*1000)
    has_frames, image = video.read()
    if has_frames: return image
