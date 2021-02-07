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
