from yattag import Doc
from yattag import indent

data = {}
data["form_defaults"] = ""
data["form_errors"] = ""
data["article"] = {}
data["article"]["title"] = ""
data["article"]["description"] = ""
data['user'] = {}
data['user']['username'] = ""

# def connection_box(data):

#     doc, tag, text, line = Doc().ttl()

#     with tag('div', id = 'connection-box'):
#         if data['user']:
#             text('Hello ', data['user']['username'], '!')
#         else:
#             with tag('form', action = '/connect'):
#                 line('label', 'Username:')
#                 doc.input('username', type = 'text')

#                 line('label', 'Password:')
#                 doc.input('password', type = 'password')

#                 doc.stag('input', type = 'submit', value = 'Connexion')

#     return doc.getvalue()

def display_article(data):

    doc, tag, text, line = Doc(
        defaults = data['form_defaults'],
        errors = data['form_errors']
    ).ttl()

    doc.asis('<!DOCTYPE html>')

    with tag('html'):

        with tag('body'):

            line('h1', data['article']['title'])

            with tag('div', klass = 'description'):
                text(data['article']['description'])

            with tag('form', action = '/add-to-cart'):
                doc.input(name = 'article_id', type = 'hidden')
                doc.input(name = 'quantity', type = 'text')

                doc.stag('input', type = 'submit', value = 'Add to cart')

    return doc.getvalue()


result = display_article(data)
print(type(result))
result = indent(
    result,
    indentation = '    ',
    newline = '\r\n',
    indent_text = True
)
print(result)
