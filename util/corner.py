# -*- coding: utf-8 -*-
import sys
import numpy as np
import cv2
# from matplotlib import pyplot as plt

# Give an edge image
# Return a list of detected corners
def detect_corners(image, threshold, dectector_type=cv2.FAST_FEATURE_DETECTOR_TYPE_5_8):
	fast = cv2.FastFeatureDetector(threshold, False)
	# fast.setBool('nonmaxSuppression',0)
	return fast.detect(image, None)

if __name__ == "__main__":
	img = cv2.imread(sys.argv[1],0)

	kp = detect_corners(img)
	img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))

	cv2.imwrite('fast_true.png',img2)