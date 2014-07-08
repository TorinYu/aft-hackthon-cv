#!/usr/bin/python

import sys
import cv2

def preprocess(image):
    mv = cv2.split(image)
    mv[0] = cv2.equalizeHist(mv[0])
    mv[1] = cv2.equalizeHist(mv[1])
    mv[2] = cv2.equalizeHist(mv[2])
    color = cv2.merge(mv)
    return color

if __name__ == "__main__":
    cv2.imwrite(sys.argv[2], preprocess(cv2.imread(sys.argv[1])))
