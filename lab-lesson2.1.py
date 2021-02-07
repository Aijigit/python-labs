import re

print("\nНайти самого длинного слова в строке")
string = "Питон самый лучший ЯП в мире!"
word_pattern = "\w+"

regex = re.compile(word_pattern)
words_found = regex.findall(string)

if words_found:
    longest_word = max(words_found, key=lambda word: len(word))
    print("Самая длинная слова => " + longest_word)
print("\n\n ")
print("Найти самого длинного слова в строке, разделенной точкой запятой.")
s = "Питон; Java; GoogleGo; PHP7; Kotlin; world!;"
s=s.strip()
st=[]
for i in range(len(s)):
    n=s.find("; ")
    if n==-1:
        st.append(s)
        break
    st.append(s[:n])
    s=s[n+1:]
    s=s.lstrip()
at=[]
max_l=0
for i in range(len(st)):
    if len(st[i])>max_l:
        at=[]
        at.append(st[i])
        max_l=len(st[i])
    elif len(st[i])==max_l:
        at.append(st[i])
if len(at)>1:
    print('ошибка: в предложении есть несколько слов максимальной длины')
else:
    print("Самая длинная слова => " + str(at[0]))

print("\n\n\nНайти самого короткого слово. И выделить его!\n\n")
s = 'Кыргызский Технический университет'
l = s.split()
word = min(l, key=len)
first = word[0]
last = len(word)
print("Найден самое короткое слово.")
symbol = str(input("Введите знак короткое вы хотите выделить! => "))
for i in range(len(word)):
	if i < len(first):
		print("Самое короткое слово => " + symbol + word + symbol) 