#!/usr/bin/env python
import cv2
import random
import os
import numpy as np
def checkEmpty(file):
    return os.stat(file).st_size == 0

def isClose(a, b, rel_tol=.01, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def cropBorders(file):
	im = cv2.imread(file)
	ids = im.copy()
	height, width = im.shape[:2]
	im[im == 255] = 1
	im[im == 0] = 255
	im[im == 1] = 0
	im2 = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(im2,125,255,0)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	y_min = 100000
	y_max = 0
	x_min = 100000
	x_max = 0
	for i in range(0, len(contours)):
	   cnt = contours[i]
	   #mask = np.zeros(image2.shape,np.uint8)
	   #cv2.drawContours(mask,[cnt],0,255,-1)
	   x,y,w,h = cv2.boundingRect(cnt)
	   if x_min > x:
	       x_min = x			
	   if x_max < x + w:
	       x_max = x + w			
	   if y_min > y:
	       y_min = y			
	   if y_max < y + h:
	       y_max = y + h			
	       
	return ids[y_min:y_max, x_min:x_max]

def fileName(f_name):
	count = 0
	sc = f_name
	temp_name = f_name.split('.')[0] + '_' + str(count) + '.png'
	while 1: 
		if not os.path.isfile(temp_name):
			return temp_name
		else:
			count += 1 
			temp_name = f_name.split('.')[0] + '_' + str(count) + '.png'
			# temp_name = f_name.split('.')[-2].split('_')
			# temp_name[-1] =  str(int(temp_count) + 1)
			# f_name =  temp_name.join()



def cropAndSave(image, x_offset, y_offset, width, height, file_name):
	save_dir = 'cropped_images/'
	crop = image[y_offset : height, x_offset : x_offset + width]
    # file_name = Dir + im + str(int(random.random()*10000)) + ".png"
	cv2.imwrite(fileName(save_dir + file_name), crop)
	# if checkEmpty(fileName(save_dir + file_name)):
	# 	print file_name + " X offset:" + str(x_offset) + "width:" +str(width)

def createBigrams(image, x_min, x_max, word_size, width, height, file_name):
	bigram_sz = float(x_max-x_min) * 2 / (word_size)
	unigram_sz = float(x_max-x_min) / (word_size)
	# print "Bigram size = %f" %(bigram_sz) 
	# Check value of delta !
	delta  = word_size
	
	num_windows = word_size / 2
	window_size = bigram_sz
	left_pos = x_min
	even_flag = False
	while left_pos + window_size <= x_max:
		for i in range(num_windows):
			if left_pos + (i+1)*window_size <= width:
				if even_flag:
					temp_name = file_name.split('/')[-1].split('.')[0] + '_' + str(2*i + 2)  + '.png' 
					cropAndSave(image, left_pos + i*window_size, 0, window_size, height, temp_name)
				else:
					temp_name = file_name.split('/')[-1].split('.')[0] + '_' + str(2*i + 1)  + '.png'
					cropAndSave(image, left_pos + i*window_size, 0, window_size, height, temp_name)
		left_pos = left_pos + delta
		if left_pos - x_min > (unigram_sz + bigram_sz) * 0.5:
			even_flag = True
		if left_pos - x_min > (bigram_sz):
			break	

# to find x_max and x_min from image!
def openImageAndExecute(path):

	for filename in os.listdir(path):
		file = path + '/' + filename
		cropped_image = cropBorders(file)
		# Change these hardcoded values!
		height, width = cropped_image.shape[:2]
		x_min = 0
		x_max = width
		wz = 9
		
		# cv2.imshow('C', cropped_image)
		# cv2.waitKey(0)
		createBigrams(cropped_image, x_min, x_max, wz, width, height, file)


Dir = '/home/vaibhav/Documents/test_folder/Images'
openImageAndExecute(Dir)
# '_' + str(int(random.random()*10000)) +



                