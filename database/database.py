import xml.etree.ElementTree as et
import csv

print("hello world")
with open('courses only.csv') as f :
	r = csv.reader(f)
	i=0
	for row in reader :
		if i<9 :
			print(row)
			i=i+1
		else :
			print("bye")
			break
