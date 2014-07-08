# -*- coding: utf-8 -*-
import os
import sys

def get_paired_images(imgdir):
	pairs = []
	for imgfile in os.listdir(imgdir):
		imgpath = os.path.join(imgdir, imgfile)
		if imgfile.endswith("inbound.jpg"):
			img1 = imgpath
			img2 = os.path.join(imgdir, imgfile.replace("inbound.jpg", "outbound.jpg"))
			assert(os.path.exists(img2))
			pairs.append((img1, img2))
		elif imgfile.endswith("before.jpg"):
			img1 = imgpath
			img2 = os.path.join(imgdir, imgfile.replace("before.jpg", "later.jpg"))
			assert(os.path.exists(img2))
			pairs.append((img1, img2))
	return pairs

if __name__ == "__main__":
	print get_paired_images(sys.argv[1])