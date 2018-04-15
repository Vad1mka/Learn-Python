from libs import keys, keys1

text = input("Введите текст для для разшифровки:")

decrypt=""
for i in text:
	#f i in keys1:
		decrypt+=keys1[i]
print("Разшифрованный текст:\n"+decrypt)
input("Нажмите Enter, чтобы закрыть программу")


