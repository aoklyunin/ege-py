# операция импликации(следования)
def impl(a, b):
    return not a or b


# минимальная длина интервала
minRange = 200

# перебираем начало интервала
for A0 in range(-1000, 100):
    # перебираем конец интервала
    for A1 in range(A0 + 1, 100):
        # переменная, отвечающая на вопрос, истинно ли выражение
        # для любых при при заданном A
        f = True
        # перебираем значения x
        for x in range(-100, 100):
            # если выражение ложно
            if not (impl(x >= A0 and x <= A1, x * x <= 64) and
                    impl(x * x <= 25, x >= A0 and x <= A1)):
                # помещаем в переменную ответ, что выражение
                # истинно не для всех x
                f = False
                # заканчиваем перебор x
                break

        # если выражение оказалось истинным для всех x
        if f:
            # если минимальная длина диапазона меньше
            # длины текущего
            if minRange > A1 - A0:
                # сохраняем новую длину
                minRange = A1 - A0

print(minRange)