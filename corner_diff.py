# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np
from functools import wraps

from util import corner, test, laplacian, colorpreocess

def get_closest_pt(pt, pts):
	dist_2 = np.sum((pts - pt)**2, axis=1)
	return pts[np.argmin(dist_2)]

def filter_kp_by_diam(kps, threshold):
	return [kp for kp in kps if kp.size > threshold]

def edge(minVal, maxVal):
	def _decorator(func):
		def _wrapper(before, after):
			before = cv2.Canny(before, minVal, maxVal)
			after = cv2.Canny(after, minVal, maxVal)
			return func(before, after)
		return _wrapper
	return _decorator

def denoise(h):
	def _decorator(func):
		def _wrapper(before, after):
			before = cv2.fastNlMeansDenoisingColored(before, h=h)
			after = cv2.fastNlMeansDenoisingColored(after, h=h)
			return func(before, after)
		return _wrapper
	return _decorator

def blur(ksize):
	def _decorator(func):
		def _wrapper(before, after):
			before = cv2.blur(before, ksize)
			after = cv2.blur(after, ksize)
			return func(before, after)
		return _wrapper
	return _decorator

def color(func):
	def _wrapper(before, after):
		before = colorpreocess.preprocess(before)
		after = colorpreocess.preprocess(after)
		return func(before, after)
	return _wrapper

def drawKeyPoints(image, kps):
	for kp in kps:
		x, y = kp.ravel()
		cv2.circle(image, (x, y), 4, 255, -1)
	return image

@denoise(10)
def _get_distance(before, after):

	# Get lists of key points (corners)
	threshold = 50
	# before_kp = corner.detect_corners(before, threshold)
	# after_kp = corner.detect_corners(after, threshold)

	before = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
	after = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

	before_kp = cv2.goodFeaturesToTrack(before, 4, 0.01, 10)
	after_kp = cv2.goodFeaturesToTrack(after, 4, 0.01, 10)

	kp_len = min(len(before_kp), len(after_kp))

	before_features = drawKeyPoints(before, before_kp)
	after_features = drawKeyPoints(after, after_kp)
	cv2.imwrite('before_features.jpg', before_features)
	cv2.imwrite('after_features.jpg', after_features)

	before_kp_pts = np.asarray([kp.ravel() for kp in before_kp[:kp_len-1]])
	after_kp_pts = np.asarray([kp.ravel() for kp in after_kp[:kp_len-1]])

	total_distance = 0
	for pt in before_kp_pts:
		closest_pt = get_closest_pt(pt, after_kp_pts)
		dist = np.sqrt((pt[0] - closest_pt[0])**2 + (pt[1] - closest_pt[1])**2)
		# print pt, closest_pt, dist
		total_distance += dist

	return total_distance/kp_len, kp_len

def print_distance(before, after):
	th = 35
	dist = _get_distance(before, after)
	if dist > th:
		print 100
	print 0

if __name__ == "__main__":
	pairs = test.get_paired_images(sys.argv[1])
	total = 0
	for (img1, img2) in pairs:
		before = cv2.imread(img1)
		after = cv2.imread(img2)
		dist, kp_len = _get_distance(before, after)
		total += dist
		print dist, kp_len
	print "Average: ", total/len(pairs)
