# операция импликации(следования)
def impl(a, b):
    return not a or b


# перебираем значения A
for A in range(1, 1000):
    #  переменная, отвечающая на вопрос, истинно ли выражение
    #  для любых при при заданном A
    f = True
    # перебираем значения k
    for k in range(1, 1000):
        if not f:
            break
        for n in range(1, 1000):
            # print(k , " " , n)
            # если выражение ложно
            if not ((5 * k + 6 * n > 57) or ((k <= A) and (n < A))):
                # помещаем в переменную ответ, что выражение
                # истинно не для всех x
                f = False
                # заканчиваем перебор x
                break

    # если выражение оказалось истинным для всех x
    if f:
        # выводим A
        print(A)
        # заканчиваем перебор
        break
