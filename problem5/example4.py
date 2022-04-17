# множество значений
values = set()

# перебираем значения от 500 до 5000, чтобы 5000 тоже было проверено,
# в качестве верхней границы я указал следующее за ним число
for i in range(500, 5001):
    # переводим строку в двоичную систему счисления
    s = bin(i)
    # обрезаем строку
    s = s[1:]
    # переводим обрезанную строку обратно в число, второй
    # аргумент указывает, в какой системе счисления записано число
    r = int(s, 2)
    # выводим разность
    values.add(r)

# перебираем значения множества
for v in values:
    # и выводим их
    print(v)
