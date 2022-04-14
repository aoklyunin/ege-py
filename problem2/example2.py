import itertools

# имена колонок
names = ['x', 'y', 'z', 'w']


# операция импликации(следования)
def impl(a, b):
    return not a or b


# логическая функция, аргументы которой мы подбираем
def f(x, y, z, w):
    return (x or y) and (y != z) and not w


# проверка значений в линии на совпадение
def find_line(xV, yV, zV, wV, f, combinations):
    if xV and zV and f and combinations[0] is None:
        return 0
    # обязательно надо сначала проверить эту строку, потому что она
    if not xV and yV and not wV and f and combinations[1] is None:
        return 1
    if yV and zV and not wV and f and combinations[2] is None:
        return 2

    return -1

# обработка перестановки
def process_permutation(p):
    # найденные комбинации
    combinations = [None] * 16
    # кол-во найденных комбинаций
    foundCombinationCnt = 0
    # перебираем все варианты значений для каждой логической переменной
    # из таблицы истинности, значений всего два: true и false
    for xV0 in [0, 1]:
        for yV0 in [0, 1]:
            for zV0 in [0, 1]:
                for wV0 in [0, 1]:
                    # чтобы использовать перестановку, построим на основе четырёх логических
                    # переменных массив
                    values = [xV0, yV0, zV0, wV0]

                    # получим значения логических переменных с учётом перестановки
                    # т.е. мы по сути формируем строку значений, которую потом будем сверять с данной
                    xV = values[p[0]]
                    yV = values[p[1]]
                    zV = values[p[2]]
                    wV = values[p[3]]
                    # ищем подходящую строку таблицы
                    lineNum = find_line(xV, yV, zV, wV, f(xV0, yV0, zV0, wV0), combinations);
                    # если строка найдена и ещё не сохранена соответствующая этой строке комбинация
                    if lineNum != -1:
                        # сохраняем комбинацию
                        combinations[lineNum] = values
                        foundCombinationCnt = foundCombinationCnt + 1

    # если найдено три комбинации
    if foundCombinationCnt == 3:
        print("++++++++++++++++++++++++++++++")
        print(p)
        # выводим шапку
        s = ""
        for i in range(4):
            s += names[p[i]] + " "
        print(s)

        # выводим сохранённые комбинации
        for i in range(3):
            s = ""
            for j in range(4):
                s += str(combinations[i][p[j]]) + " "

            print(s)


# получаем все перестановки
permutations = list(itertools.permutations([0, 1, 2, 3]))
# перебираем перестановки
for permutation in permutations:
    process_permutation(permutation)
