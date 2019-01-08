# pip install html5print

from lxml import etree
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

html_str = etree.tostring(root, pretty_print=True, xml_declaration=False)

#インデントはライブラリに頼った。
from html5print import HTMLBeautifier
html_str = HTMLBeautifier.beautify(html_str, 4)

with open('output002.html', 'w') as f:
    f.write(html_str)

# 結果
# <html>
#     <head>
#     </head>
#     <body>
#         <section>
#             section1 text
#             <section>
#                 section2 text
#             </section>
#         </section>
#     </body>
# </html>

