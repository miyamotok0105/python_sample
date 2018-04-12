from yattag import Doc
doc, tag, text, line = Doc().ttl()

with tag('ul', id='grocery-list'):
    line('li', 'Tomato sauce', klass="priority")
    line('li', 'Salt')
    line('li', 'Pepper')
print(doc.getvalue())