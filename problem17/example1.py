# кол-во нужных нам чисел
cnt = 0
# максимальное число
max = -1

# перебираем все зхначения интервала
# !обязательно доюавьте +1 в диапазон! иначе последнее число не учтётся
for i in range(1016, 7937 + 1):
    # если число нам подходит
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        # увеличиваем кол-во на 1
        cnt = cnt + 1
        # сохраняем число в максимум, т.к. перебор
        # идёт в сторону возрастания, то последнее подходящее
        # число и будет максимальным
        max = i

# выводим результат
print(cnt, max)
