from yattag import Doc
from yattag import indent

doc, tag, text, line = Doc().ttl()

with tag('ul', id='grocery-list'):
    line('li', 'Tomato sauce', klass="priority")
    line('li', 'Salt')
    line('li', 'Pepper')

result = indent(doc.getvalue())
print(result)


result = indent(
    doc.getvalue(),
    indentation = '    ',
    newline = '\r\n',
    indent_text = True
)
print(result)
