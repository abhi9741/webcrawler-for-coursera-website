import xml.etree.ElementTree as et
import csv

print("hello world")
with open('courses only.csv') as f :
	wf = open("coursedatabase.xml",'wb')
	data = et.Element('data')
	r = csv.reader(f)
	i=0
	for row in r :
		if i == 0 :
			i=i+1
			continue
		else :
			# print(row)
			course = et.SubElement(data,'course')
			item1 = et.SubElement(course,'coursetitle')
			item2 = et.SubElement(course,'coourselink')
			item3 = et.SubElement(course,'about')
			item4 = et.SubElement(course,'targetaudience')
			item5 = et.SubElement(course,'creators')
			item6 = et.SubElement(course,'instructordetails')
			item7 = et.SubElement(course,'basicinfo')
			item8 = et.SubElement(course,'level')
			item9 = et.SubElement(course,'startdate')
			item10 = et.SubElement(course,'duration')
			item11 = et.SubElement(course,'language')
			item12 = et.SubElement(course,'howtopass')
			item13 = et.SubElement(course,'review')
			item14 = et.SubElement(course,'hardwarerequired')
			item15 = et.SubElement(course,'syllabus')
			item16 = et.SubElement(course,'pricing')

			


			item1.text = row[0]
			item2.text = row[1]

			k=row[2]
			k=k.split('\n')
			k=' '.join(k)
			# k=k.split('&#8217;')
			# k=' '.join(k)
			item3.text = k
			item4.text = row[3]
			item5.text = row[4]
			k=row[5]
			k=k.split('\n\xa0\xa0')
			# print(k)
			try:
				k=k[1]
			except :
				pass
			k=''.join(k)
			# print(k)
			# k=k.split('\n')
			# k=' '.join(k)
			item6.text = k

			k=row[6]
			# k=k.split('\n')
			# k=' '.join(k)
			item7.text = k

			item8.text = row[7]
			item9.text = row[8]
			item10.text = row[9]
			item11.text = row[10]
			item12.text = row[11]
			k=row[12].split("learners said")
			k=k[0]+" learners said : "+item2.text +"#ratings" 
			item13.text = k
			item14.text = row[13]

			k=row[14]
			# k=k.split('\n')
			# k=' '.join(k)
			# item15.text = k
			item16.text = row[15]
			
			

			i=i+1
			print(i)
		
	mydata=et.tostring(data)
	#myfile = open("course_write_eg.xml",'wb')
	wf.write(mydata)