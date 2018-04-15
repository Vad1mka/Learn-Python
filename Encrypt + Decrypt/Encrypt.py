from libs import keys, keys1



# Шифрование
text = input("Введите текст для шифрования: ")
crypt=""
for i in text:
	if i in keys:
		crypt+=keys[i]
print("Зашифрованный текст:\n"+crypt+"\n")
input("Нажмите Enter, чтобы закрыть программу")
#Работает только с английским алфавитом



