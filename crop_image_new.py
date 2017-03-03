import numpy as np
import cv2
import os

Dir = '/home/vaibhav/Documents/test_folder/Images'
results = list()
for path, subdirs, files in os.walk(Dir):
    for filename in files:
        if os.path.splitext(filename)[1] == '.png':
            f = os.path.join(path, filename)
            results.append(f)

files = results

for file in files:
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
	   #mask = np.zeros(im2.shape,np.uint8)
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
	       
	print file
	file_path = "/".join(file.split('/')[-2:])
	if not os.path.exists('cropped/'+file_path.split('/')[0]):
		os.makedirs('cropped/'+(file_path.split('/')[0]))
	cv2.imwrite('cropped/'+file_path, ids[y_min:y_max, x_min:x_max])

