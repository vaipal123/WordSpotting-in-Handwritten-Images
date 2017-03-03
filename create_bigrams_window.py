#!/usr/bin/env python
import cv2
import random
import os
def check_empty(file):
    return os.stat(file).st_size == 0

def isclose(a, b, rel_tol=.1, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def crop_save_image(image, x_offset, y_offset, width, height):
    # image_path = "~/Documents/bigram_images/"
    Dir  = '/home/vaibhav/Documents/bigram_images/'
    im = 'image_'
    crop = image[0:height, x_offset:width]
    file_name = Dir + im + str(int(random.random()*10000)) + ".png"
    cv2.imwrite(file_name, crop)
    if check_empty(file_name):
        print file_name + " X offset:" + str(x_offset) + "width:" +str(width)

def sliding_window(image, bigram_size, unigram_size, height, width, word_size):
    X_MIN = 0
    X_MAX = width
    window = bigram_size
    k = 10
    delta = float(unigram_size/k)
    x_min = 0
    x_max = window
    i = float(0)
    print "Delta" + str(delta)

    # while x_max <= X_MAX:
    #     change_position = x_min + usz      
    #     while i + x_min <= change_position and x_max + i <= X_MAX :
    #         # print image, x_min + i, height, x_max + i, height
    #         if x_max - x_min >= window:
    #             crop_save_image(image, x_min + i, height, x_max + i, height)
    #         i = i + delta
    #     x_min = x_min + usz
    #     x_max = x_max + usz
    #     i = 0
    while x_max <= X_MAX:
        change_position = x_min + unigram_size
        if isclose(i, change_position):
            x_min = x_min + unigram_size
            x_max = x_max + unigram_size
        elif x_max + i <= X_MAX:
            crop_save_image(image, x_min + i, height, x_max + i, height)
        i = i + delta

IMG_DIR = ''
with open("final_train_xml.xml" , 'w') as XML_FILE:
# with open("final_test_xml2.xml" , 'w') as XML_FILE:
    XML_FILE.write('<wordLocations dataset="IAM">\n')
    # print arr
    for f in result:
        e = xml.etree.ElementTree.parse(f)
        for atype in e.iter('spot'):
            file = atype.get('id')
            dirs = file.split('-')
            temp = dirs[0] + '-'+ dirs[1] + '-' + dirs[2]
            if temp in arr:
                text = atype.get('text').replace('\"', "&quot;").replace('&', "&amp;")
                path = 'IAM/'+dirs[0]+'/'+dirs[0]+'-'+dirs[1]+'/'+file+'.png'
                img = cv2.imread(path)
                height, width = img.shape[:2]
                # rel_path = dirs[0]+'/'+dirs[0]+'-'+dirs[1]+'/'+file+'.png'
                rel_path = file+'.png'

                xml_line = '<spot h="'+str(height)+'" image="'+rel_path+'" w="'+str(width)+'" word="'+text+'" x="0" y="0"/>\n'
                XML_FILE.write(xml_line)
            
    XML_FILE.write('</wordLocations>')

path = 'move.png'
img = cv2.imread(path)
word_size = 4
height, width = img.shape[:2]
xmin = 0
xmax = width
bsz=float(xmax-xmin)/(word_size*.5)
usz=float(xmax-xmin)/(word_size)
print "Bigram size:" + str(bsz) + " Unigram size:" + str(usz) + " Image size " + str(width)                
sliding_window(img,bsz,usz,height,width,word_size)