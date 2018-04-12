from yattag import Doc

doc, tag, text = Doc().tagtext()

#stagはimgタグのような形式のもの。セルフクロージングタグと呼んでる。
with tag('div', id='photo-container'):
    doc.stag('img', src='./demo/32x32.gif', klass="photo")

print(doc.getvalue())
