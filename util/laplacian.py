# -*- coding: utf-8 -*-

import cv2
import numpy as np

def get_gradient(image):
	lp64f = cv2.Laplacian(image, cv2.CV_64F)
	abs_lp64f = np.absolute(lp64f)
	return np.uint8(abs_lp64f)
