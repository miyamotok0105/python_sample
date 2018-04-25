from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            if attr[0] == "style":
                print({pair.split(":")[0]:pair.split(":")[1] for pair in attr[1].split(";") if pair != ""})
            else:
                print("     attr:", attr)
        
    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
#doctype をパースします:
parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
             '"http://www.w3.org/TR/html4/strict.dtd">')
#要素のタイトルと一部属性をパースします:
parser.feed('<img src="python-logo.png" alt="The Python logo">')

parser.feed('<h1>Python</h1>')

#それ以上のパースを行わずに、script と style 要素の内容をそのまま返します:
parser.feed('<style type="text/css">#python { color: green }</style>')
parser.feed('<script type="text/javascript">'
             'alert("<strong>hello!</strong>");</script>')


#コメントをパースします:
parser.feed('<!-- a comment -->'
             '<!--[if IE 9]>IE-specific content<![endif]-->')



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




