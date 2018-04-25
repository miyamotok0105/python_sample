#define CO_MAXBLOCKS 200

from datetime import date
from yattag import Doc
doc, tag, text = Doc().tagtext()


def a():
    with tag('html'):
        with tag('head'):
            with tag('meta'):
                with tag('title'):
                    with tag('body'):
                        with tag('div'):
                            with tag('article'):
                                pass

def b():
    with tag('header'):
        with tag('div'):
            with tag('div'):
                with tag('div'):
                    with tag('img'):
                        with tag('h1'):
                            with tag('img'):
                                with tag('div'):
                                    pass

def c():
    with tag('div'):
        with tag('img'):
            with tag('ul'):
                with tag('li'):
                    with tag('a'):
                        with tag('span'):
                            with tag('sup'):
                                pass


def d():
    with tag('br'):
        with tag('li'):
            with tag('a'):
                with tag('span'):
                    with tag('br'):
                        with tag('li'):
                            with tag('a'):
                                with tag('span'):
                                    pass

def e():
    with tag('br'):
        with tag('li'):
            with tag('a'):
                with tag('span'):
                    with tag('br'):
                        with tag('div'):
                            with tag('div'):
                                with tag('img'):
                                    pass

def f():
    with tag('a'):
        with tag('div'):
            with tag('img'):
                with tag('section'):
                    with tag('a'):
                        with tag('span'):
                            with tag('section'):
                                with tag('ul'):
                                    with tag('li'):
                                        with tag('a'):
                                            with tag('img'):
                                                pass

a()
b()
c()
d()
e()
f()
print(doc.getvalue())
