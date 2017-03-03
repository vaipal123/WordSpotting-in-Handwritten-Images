#!/usr/bin/env python
import cv2
import random
import os
# def check_empty(file):
#     return os.stat(file).st_size == 0

# def isclose(a, b, rel_tol=.1, abs_tol=0.0):
#     return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

# def crop_save_image(image, x_offset, y_offset, width, height):
#     # image_path = "~/Documents/bigram_images/"
#     Dir  = '/home/vaibhav/Documents/bigram_images/'
#     im = 'image_'
#     crop = image[0:height, x_offset:width]
#     file_name = Dir + im + str(int(random.random()*10000)) + ".png"
#     cv2.imwrite(file_name, crop)
#     if check_empty(file_name):
#         print file_name + " X offset:" + str(x_offset) + "width:" +str(width)

# def sliding_window(image, bigram_size, unigram_size, height, width, word_size):
#     X_MIN = 0
#     X_MAX = width
#     window = bigram_size
#     k = 10
#     delta = float(unigram_size/k)
#     x_min = 0
#     x_max = window
#     i = float(0)
#     print "Delta" + str(delta)

#     # while x_max <= X_MAX:
#     #     change_position = x_min + usz      
#     #     while i + x_min <= change_position and x_max + i <= X_MAX :
#     #         # print image, x_min + i, height, x_max + i, height
#     #         if x_max - x_min >= window:
#     #             crop_save_image(image, x_min + i, height, x_max + i, height)
#     #         i = i + delta
#     #     x_min = x_min + usz
#     #     x_max = x_max + usz
#     #     i = 0
#     while x_max <= X_MAX:
#         change_position = x_min + unigram_size
#         if isclose(i, change_position):
#             x_min = x_min + unigram_size
#             x_max = x_max + unigram_size
#         elif x_max + i <= X_MAX:
#             crop_save_image(image, x_min + i, height, x_max + i, height)
#         i = i + delta

# IMG_DIR = 
# path = 'move.png'
# img = cv2.imread(path)
# word_size = 4
# height, width = img.shape[:2]
# xmin = 0
# xmax = width
# bsz=float(xmax-xmin)/(word_size*.5)
# usz=float(xmax-xmin)/(word_size)
# print "Bigram size:" + str(bsz) + " Unigram size:" + str(usz) + " Image size " + str(width)                
# sliding_window(img,bsz,usz,height,width,word_size)
image = cv2.imread('/home/vaibhav/Documents/test_folder/Images/word1sample1.png')
height, width = image.shape[:2]
crop = image[0:height, width/2:width]
cv2.imwrite('crop_image_test_1.png', crop)
