rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
       'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',
       "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

eng = ["a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "i", "k", "l", "m", "n", "o",
       "p", "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh", "shch", "ie", "y", "", "e", "iu", "ia",
       "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]



class Transliterator:
    def __init__(self, message):
        self.rf = rus
        self.en = eng
        self.ss = (self.rf, self.en)
        self.cc = {r: e for r, e in zip(*self.ss)}
        self.text = message

    def translate(self, text):
        while True:
            try:
                trans = ''.join([self.cc[i] for i in text])
                return trans
            except:
                return text

    def show(self):
        print(self.text)

    def __repr__(self):
        return self.translate(self.text)


    def translateFile(self, a, b):
        with open(a, 'r', encoding='utf8') as f:
            words = f.read().split()
            with open(b, 'w', encoding='utf8') as f:
                for word in words:
                    print(self.translate(word), file=f)



t = Transliterator('')

print(t.translate("экзамен"))
print(t.translate("илья"))
print(t.translate("Илья"))
print(t.translate('$'))
print(t.translate('3'))
print(t.translate('9'))
print(t.translate('0'))

t.translateFile('exam/a.txt', 'exam/b.txt')
