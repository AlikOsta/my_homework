str = "Hello Zz World!"
# str = input("Введите текст: ")
s = []
for i in str:
    if ord(i) == 90 or ord(i) == 122:
        s.append((chr(ord(i) - 25)))
    elif ord(i) == 32:
        s.append((chr(ord(i))))
    else:
        s.append((chr(ord(i) + 1)))
print("".join(s))

str_1 = 'Ifmmp Aa Xpsme"'
# str_1 = input("Введите текст: ")
s_1 = []
for i in str_1:
    if ord(i) == 65 or ord(i) == 97:
        s_1.append((chr(ord(i) + 25)))
    elif ord(i) == 32:
        s_1.append((chr(ord(i))))
    else:
        s_1.append((chr(ord(i) - 1)))
print("".join(s_1))




