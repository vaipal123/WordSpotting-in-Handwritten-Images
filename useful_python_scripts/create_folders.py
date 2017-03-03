import os

l = list()
with open('folder_names_bigrams_s.txt') as f:
	l = f.read().splitlines()

for x in l:
	os.mkdir(x)

# find /home/vaibhav/Documents/IAM_stuff/bigrams -type f -size 0c -delete