#!/usr/bin/env python
import cv2
import random
import os
from matplotlib import pyplot as plt
def openImageAndExecute(path):

	for filename in os.listdir(path):
		file = path + '/' + filename
		img = cv2.imread(file, cv2.IMREAD_COLOR)
		height, width = img.shape[:2]
		# Change these hardcoded values!
		plt.hist(img.ravel(),256,[0,256]); plt.show()


Dir = '/home/vaibhav/Documents/test_folder/Images'
openImageAndExecute(Dir)
