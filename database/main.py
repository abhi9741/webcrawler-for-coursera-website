import xml.etree.ElementTree as et

#for reading an xml file
'''
tree = et.parse("items_eg.xml")
root = tree.getroot()

print('Item #2 attribute : ')
print(root[0][1].attrib)

print('all items atributes : ')
for elem in root :
	for subelem in elem :
		print(subelem.attrib)

print('\n Item #2 data : ')
print(root[0][1].text)

print('\n all Items data : ')
for elem in root :
	for subelem in elem :
		print(subelem.text)
print("total no of items "+str(len(root)))



#for writing into an xml file

data = et.Element('data')
items = et.SubElement(data,'items')
item1 = et.SubElement(items,'item')
item2 = et.SubElement(items,'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text='item1abc'
item2.text='item2abc'

mydata = et.tostring(data)
myfile = open("read_eg.xml","wb")
myfile.write(mydata)
myfile.close()
'''

#for writing course structure into an example file
#version1
'''
data = et.Element('data')
course = et.SubElement(data,'course')
item1=et.SubElement(course,'detail')
item2=et.SubElement(course,'detail')
item3=et.SubElement(course,'detail')


item1.set('name','title')
item2.set('name','about')
item3.set('name','cost')

item1.text="god knows"
item2.text="does not matter"
item3.text="only thing that matters"

mydata=et.tostring(data)
myfile = open("course_write_eg.xml",'wb')
myfile.write(mydata)
'''
'''
data = et.Element('data')
course = et.SubElement(data,'course')
item1=et.SubElement(course,'title')
item2=et.SubElement(course,'about')
item3=et.SubElement(course,'cost')



item1.text="god knows"
item2.text="does not matter"
item3.text="only thing that matters"

mydata=et.tostring(data)
myfile = open("course_write_eg.xml",'wb')
myfile.write(mydata)
'''
#for writing more than one object
'''
data = et.Element('data')

for i in range(0,5) :

	course = et.SubElement(data,'course')
	item1=et.SubElement(course,'title')
	item2=et.SubElement(course,'about')
	item3=et.SubElement(course,'cost')

	item1.text="god knows"+str(i)
	item2.text="does not matter"+str(i)
	item3.text="only thing that matters"+str(i)

mydata=et.tostring(data)
myfile = open("course_write_eg.xml",'wb')
myfile.write(mydata)
'''

#for finding xml elements
'''
tree =et.parse("course_write_eg.xml")
root = tree.getroot()

for elem in root :
	#print(elem.find('title').text)
	for subelem in root :
		if subelem.find('cost').text == str(50) :
			print( subelem.text)

'''

tree = et.parse("coursedatabase.xml")
root = tree.getroot()

for elem in root :
	for subelem in root :
		print(subelem.find('title').text)