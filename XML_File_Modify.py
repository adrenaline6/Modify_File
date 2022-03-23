import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
def Modify():
	# This is the parent (root) tag
	# onto which other tags would be
	# created
	data = ET.Element('saranghe')

	# Adding a subtag named `Opening`
	# inside our root tag
	element1 = ET.SubElement(data, 'child', name='Frank', test=0)
	element2 = ET.SubElement(data, 'unique')
	element3 = ET.SubElement(data, 'child', name='Texas', test=1)
	element4 = ET.SubElement(data, 'child', name='Frank', test=2)
	element5 = ET.SubElement(data, 'unique')
	element6 = ET.SubElement(data, 'data')

	s_elem1 = ET.SubElement(element1, 'E4')
	s_elem2 = ET.SubElement(element1, 'D4')

	# Adding attributes to the tags under
	# `items`
	s_elem1.set('type', 'Accepted')
	s_elem2.set('type', 'Declined')

	# Adding text between the `E4` and `D5`
	# subtag
	s_elem1.text = "King's Gambit Accepted"
	s_elem2.text = "Queen's Gambit Declined"

	# Converting the xml data to byte object,
	# for allowing flushing data to file
	# stream
	b_xml = ET.tostring(data)

	# Opening a file under the name `items2.xml`,
	# with operation mode `wb` (write + binary)
	with open("GFG.xml", "wb") as f:
		f.write(b_xml)
	f.close()
def Readfile():
	with open('GFG.xml', 'r') as f:
		data = f.read()
		Bs_data = BeautifulSoup(data, 'xml')
		b_unique = Bs_data.find_all('D4')
		print(b_unique)
if __name__ == '__main__':
    	# Readfile()
		Modify()
	