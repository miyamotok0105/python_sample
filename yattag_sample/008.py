from yattag import Doc
from yattag import indent

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
    with doc.textarea(name = 'contact_message'):
        pass
    doc.stag('input', type = 'submit', value = 'Send my message')

result = indent(
    doc.getvalue(),
    indentation = '    ',
    newline = '\r\n',
    indent_text = True
)
print(result)
