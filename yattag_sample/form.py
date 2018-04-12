# coding: UTF-8
from yattag import Doc

doc, tag, text, line = Doc(
    defaults = {
        'title': 'Untitled',
        'contact_message': 'You just won the lottery!'
    },
    errors = {
        'contact_message': 'Your message looks like spam.'
    }
).ttl()

line('h1', 'Contact form')
with tag('form', action = ""):
    doc.input(name = 'title', type = 'text')
    doc._append('\n')
    with doc.textarea(name = 'contact_message'):
        pass
    doc.stag('input', type = 'submit', value = 'Send my message')
    doc._append('\n')

print(doc.getvalue())
s = doc.getvalue()

f = open('text.txt', 'w')
f.write(s)
f.close()
