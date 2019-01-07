# pip install html5print

from lxml import etree
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

root = etree.Element("html")
section1 = etree.Element("section")
section1.text = "section1 text"

section2 = etree.Element("section")
section2.text = "section2 text"

#親子関係にする。
#root->section1->section2
section1.append(section2)
root.append(section1)

print(etree.tostring(root, pretty_print=True, xml_declaration=False))

tree = ET.ElementTree(element=root)
html_str = etree.tostring(root, pretty_print=True, xml_declaration=False)

#インデントしたいなー
tree.write("output001.xml","UTF-8",False, method="html")





