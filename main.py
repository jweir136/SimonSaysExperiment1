########### IMPORT THE 3RD PARTY REQUIREMENTS ##########
import tensorflow.keras as keras
import cv2
import os

########### IMPORT THE CUSTOM REQUIREMENTS #############
from OpenPose import OpenPose

pose =  OpenPose()

if __name__ == "__main__":
  img = cv2.imread("ski.jpg")
  pose.keypoints(img)
