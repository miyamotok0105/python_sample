from yattag import Doc
from yattag import indent

doc, tag, text, line = Doc(
    defaults = {'color': 'red', 'fun': 'yes'},
    errors = {'shipping-method':\
      "Error! You're an idiot for not having chosen a shipping method."
    }
).ttl()

line('h1', 'Spaceship delivery details')
with tag('form', action = ""):

    line('p', 'Please pick the color of the spaceship')
    for color in ('blue', 'red', 'pink', 'yellow', 'ugly-yellow'):
        doc.input(name = 'color', type = 'radio', value = color)
        text(color)

    line('p', 'What shipping method should be used?')
    doc.input(name = 'shipping-method', type = 'radio', value = '1')
    text('Priority mail')
    doc.input(name = 'shipping-method', type = 'radio', value = '2')
    text('Delivery by a very old monk travelling on a horse')

    with tag('p'):
        text("Check this box if you want some additional fun for free")
        doc.input(name = 'fun', type = 'checkbox', value = 'yes')

    doc.stag('input', type = 'submit', value = 'Confirm my order')

result = indent(
    doc.getvalue(),
    indentation = '    ',
    newline = '\r\n',
    indent_text = True
)
print(result)
