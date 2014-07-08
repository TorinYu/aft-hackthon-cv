import sys
import cv2
import numpy as np
# from matplotlib import pyplot as plt

# Return an edge image
def detect_edges(image, minVal=100, maxVal=200):
	return cv2.Canny(image, minVal, maxVal)


if __name__ == "__main__":
	img = cv2.imread(sys.argv[1], 0)
	edges = detect_edges(img)
	cv2.imwrite(sys.argv[2], edges)
	# plt.subplot(121),plt.imshow(img,cmap = 'gray')
	# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
	# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

	# plt.show()