from yattag import Doc

doc, tag, text = Doc().tagtext()

#asisで特殊文字エスケープ。
doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('body'):
        text('Hello world!')

print(doc.getvalue())
