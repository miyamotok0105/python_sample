from cssselect import GenericTranslator, SelectorError
try:
    expression = GenericTranslator().css_to_xpath('div.content')
except SelectorError:
    print('Invalid selector.')
print(expression)


from lxml.etree import fromstring
document = fromstring('''
   <div id="outer">
     <div id="inner" class="content body">text</div>
   </div>
 ''')
print([e.get('id') for e in document.xpath(expression)])

#=========================

from lxml import etree
try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")


root = etree.Element("root")
print(root.tag)

#=========================

html = etree.Element("html")
body = etree.SubElement(html, "body")
body.text = "TEXT"

print(etree.tostring(html))
#b'<html><body>TEXT</body></html>'

br = etree.SubElement(body, "br")
print(etree.tostring(html))
#b'<html><body>TEXT<br/></body></html>'

br.tail = "TAIL"
print(etree.tostring(html))
#b'<html><body>TEXT<br/>TAIL</body></html>'


#=========================


attr_string ="fill:#00ff00;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"
attr_dict = {pair.split(":")[0]:pair.split(":")[1] for pair in attr_string.split(";")}
print(attr_dict)

attr_string ="display:inline;margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;border-width:0;font-style:normal;font-weight:normal;font-size:100%;vertical-align:baseline;"
attr_dict = {pair.split(":")[0]:pair.split(":")[1] for pair in attr_string.split(";") if pair != ""}
print(attr_dict)

# print([i for i in attr_string.split(";") if i != ""])
# print(attr_string.split(";"))
# l = attr_string.split(";")
# for i in l:
#     print(i)
#=========================

# from io import StringIO, BytesIO
# html = ""
# f = open('001.html','r')
# for row in f:
#     html += row
# f.close()

# parser = etree.HTMLParser()
# tree   = etree.parse(StringIO(html), parser)

# result = etree.tostring(tree.getroot(),
#                          pretty_print=True, method="html")
# # print(result)
# print(tree)



#=========================
#=========================
#=========================
#=========================


