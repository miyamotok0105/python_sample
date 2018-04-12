from yattag import Doc

from datetime import date
today = date.today()

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        if today.month == 1 and today.day == 1:
            #attrで同じ階層のタグに属性追加。
            doc.attr(klass = "new-year-style")
        else:
            doc.attr(klass = "normal-style")
        text("Welcome to our site")

print(doc.getvalue())