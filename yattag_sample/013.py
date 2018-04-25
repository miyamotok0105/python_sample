from yattag import Doc
doc, tag, text = Doc().tagtext()
with tag('div', id='photo-container'):
    doc.stag('img', src='./demo/32x32.gif', klass="photo")
print(doc.getvalue())


import sys, string
class CodeGeneratorBackend:
    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        return "".join(self.code)

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError("internal error in code generator")
        self.level = self.level - 1

# c = CodeGeneratorBackend()
# c.begin(tab="    ")
# c.write("for i in range(10):\n")
# c.indent()
# c.write("print('code generation is trivial')")
# c.dedent()
# print(c.end())

# exec(c.end())

#==============================
# from yattag import Doc
# doc, tag, text = Doc().tagtext()
# with tag('div', id='photo-container'):
#     doc.stag('img', src='./demo/32x32.gif', klass="photo")
# print(doc.getvalue())

c = CodeGeneratorBackend()
c.begin(tab="    ")
c.write("from yattag import Doc\n")
c.write("doc, tag, text = Doc().tagtext()\n")
c.write("with tag('div', id='photo-container'):\n")
c.indent()
c.write('doc.stag("img", src="./demo/32x32.gif", klass="photo")\n')
c.dedent()
c.write("print(doc.getvalue())\n")
# print(c.end())

exec(c.end())




