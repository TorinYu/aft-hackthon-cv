#!/usr/bin/python

import sys
import cv2

def preprocess(image):
    grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(grayed)
    return equalized

if __name__ == "__main__":
    cv2.imwrite(sys.argv[2], preprocess(cv2.imread(sys.argv[1])))
