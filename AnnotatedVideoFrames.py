import cv2
from OpenPose import OpenPose

class AnnotatedVideoFrames:
    def __init__(self):
        self.frames = []
        self.temp_frames = None
        self.temp_height = None

    def height(self, keypoints):
        min_ = min([arr[1] for arr in keypoints if arr[1] != 0 and arr[1] != -1])
        max_ = max([arr[1] for arr in keypoints if arr[1] != 0 and arr[1] != -1])
        return max_ - min_

    def add_frame(self, keypoints):
        h = self.height(keypoints)
        self.frames.append(
            [keypoints[i] / h for i in range(len(keypoints))]
        )

    def clear(self):
        self.frames = []
        self.temp_frames = None
        self.temp_height = None
