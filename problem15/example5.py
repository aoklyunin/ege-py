# операция импликации(следования)
def impl(a, b):
    return not a or b


# перебираем значения A
for a in range(1, 1000):
    # переменная, отвечающая на вопрос, истинно ли выражение
    # для любых при при заданном a
    f = True
    # перебираем значения x
    for x in range(1, 1000):
        # если выражение ложно
        if not (((x & 125) != 1) or impl((x & 34) == 2, (x & a) == 0)):
            # помещаем в переменную ответ, что выражение
            # истинно не для всех x
            f = False
            # заканчиваем перебор x
            break

    # если выражение оказалось истинным для всех x
    if f:
        # выводим a
        print(a)
        # заканчиваем перебор
        break
