import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
def Modify():
	# This is the parent (root) tag
	# onto which other tags would be
	# created
	data = ET.Element('saranghe')

	# Adding a subtag named `Opening`
	# inside our root tag
	element1 = ET.SubElement(data, 'child')
	element1.set('name', 'Frank')
	element1.set('test', '0')
	element1.text = 'FRANK likes EVERYONE'
	element2 = ET.SubElement(data, 'unique')
	element2.text = 'Add a video URL here'
	element3 = ET.SubElement(data, 'child')
	element3.set('name', 'Texas')
	element3.set('test', '1')
	element3.text = 'TEXAS is a PLACE'
	element4 = ET.SubElement(data, 'child')
	element4.set('name', 'Frank')
	element4.set('test', '2')
	element4.text = 'Exclusively'
	element5 = ET.SubElement(data, 'unique')
	element5.text = 'Add a workbook URL here'

	element6 = ET.SubElement(data, 'data')
	element6.text = 'Add the content of your article here'
	ele_data_1 = ET.SubElement(element6, 'family')
	ele_data_1.text = 'Add the font family of your text here'
	ele_data_2 = ET.SubElement(element6, 'size')
	ele_data_2.text = 'Add the font size of your text here'	

	# Adding attributes to the tags under
	# `items`


	# Adding text between the `E4` and `D5`
	# subtag


	# Converting the xml data to byte object,
	# for allowing flushing data to file
	# stream
	b_xml = ET.tostring(data)

	# Opening a file under the name `items2.xml`,
	# with operation mode `wb` (write + binary)
	with open("test.xml", "wb") as f:
		f.write(b_xml)
	f.close()
def Readfile():
	with open('test.xml', 'r') as f:
		data = f.read()
		Bs_data = BeautifulSoup(data, 'xml')
		b_unique = Bs_data.find_all('D4')
		print(b_unique)
if __name__ == '__main__':
    	# Readfile()
		Modify()
	