a = str(input('Введите текст: '))
b = str(input('Введите заданное слово: '))
c = 0
for i in range(len(a)):
	if a[i: i + len(b)] == b:
		c += 1
print("Количество заданных слов = ", c)
