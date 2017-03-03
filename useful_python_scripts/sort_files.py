l = list()
with open('folder_names_bigrams.txt') as f:
	l = f.readlines()

l.sort()

with open('folder_names_bigrams_s.txt','w') as f:
	for x in l:
		f.write(x)
