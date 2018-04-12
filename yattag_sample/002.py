from yattag import Doc

doc, tag, text = Doc().tagtext()

#tagに任意の名前つけれる。withの中に入れれば入れ子になる。textで文字が入る。
doc._append('\n')
#<icecream id="2" flavour="pistachio">This is really delicious.</icecream>
with tag('icecream', id = '2', flavour = 'pistachio'):
    text("This is really delicious.")

#idはidでsosoなど任意の名前をつけることも可能。
doc._append('\n')
with tag('div', id = '2', soso = 'soso'):
    text("This is really delicious.")

#klassでclass
doc._append('\n')
with tag('h2', klass='breaking-news'):
    text('Sparta defeats Athens')

doc._append('\n')
with tag('td',
    ('data-search', 'lemon'),
    ('data-order', '1384'),
    id = '16'
):
    text('Citrus Limon')

doc._append('\n')
with tag('html', 'ng-app'):
    with tag('body'):
        text('Welcome to my AngularJS application.')
        username = "aaaaa"
        #当然埋め込める
        text('Hello ', username, '!')


print(doc.getvalue())
