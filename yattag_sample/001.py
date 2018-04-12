from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('h1'):
    text('Hello world!')

print(doc.getvalue())
