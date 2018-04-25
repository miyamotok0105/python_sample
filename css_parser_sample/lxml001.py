#!/usr/bin/env python
import sys
from lxml import etree as et

HTML_NS  =  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
XSL_NS   =  "http://www.w3.org/1999/XSL/Transform"
NS_MAP = {None:  HTML_NS,
          "xsl": XSL_NS}

rootName = et.QName(XSL_NS, 'stylesheet')
root = et.Element(rootName, nsmap=NS_MAP)
sheet = et.ElementTree(root)

top = et.SubElement(root, et.QName(XSL_NS, "template"), match='/')
html = et.SubElement(top, et.QName(HTML_NS, "html"))
head = et.SubElement(html, "head")
title = et.SubElement(head, "title")
title.text = "Heading title"
body = et.SubElement(html, "body")
h1 = et.SubElement(body, "h1")
h1.text = "Body heading"
p = et.SubElement(body, "p")
p.text = "Paragraph text"
sheet_str = et.tostring(sheet)
print(sheet_str)



