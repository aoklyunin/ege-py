# задаём значение
x = 4 ** 512 + 8 ** 512 - 2 ** 128 - 250
# кол-во шетёрок равно 0
count0 = 0
# пока число больше 0
while x:
    # если остаток от деления на 7 равен 0
    if x % 2 == 0:
        # увеличивае кол-во
        count0 += 1
    # делим число на 7
    x //= 2
# выводим ответ
print(count0)