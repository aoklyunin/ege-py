# операция импликации(следования)
def impl(a, b):
    return not a or b


# логическая функция, аргументы которой мы подбираем
def f(x, y, z):
    return impl(x, y) and impl(y, z)


# выводим заголовок
print("x y z")
# перебираем все наборы значений
for xV0 in [0, 1]:
    for yV0 in [0, 1]:
        for zV0 in [0, 1]:
            # если функция даёт ложь
            if not f(xV0, yV0, zV0):
                # выводим этот набор аргументов
                print(str(xV0) + " " + str(yV0) + " " + str(zV0))
