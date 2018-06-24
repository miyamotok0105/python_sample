# coding: UTF-8
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        #findallは正規表現に一致する重複のない文字列のリストを返す
        self.words = RE_WORD.findall(text)  # <1>

    #インデクシングの処理のフックメソッド
    def __getitem__(self, index):
        return self.words[index]  # <2>

    def __len__(self, index):  # <3>
        return len(self.words)

    #オブジェクトの返す処理
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # <4>

if __name__ == '__main__':
    s = Sentence("jihfowjfi!!JOIJ!!!!IO")
    print(s)

    print("=======")
    s = Sentence("The time ha ... war said")
    for word in s:
        print(word)
    print("=======")
    print(list(s))
    print(len(list(s)))
    print(list(s)[0])
    print(list(s)[-1])

    print("=======")
    it = iter(s)
    print(next(it))
    print(next(it))
