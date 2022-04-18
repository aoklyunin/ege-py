import itertools

# множество кодов
values = set()


# обработка перестановки
def process_permutation(arr):
    # кол-во повторяющихся символов
    c = 0
    # строка с кодом
    s = ""
    for i in range(len(arr) - 1):
        # если текущий символ равен предыдущему
        if arr[i] == arr[i + 1]:
            # увеличиваем кол-во повторяющихся функций
            c = c + 1
        # прибавляем текущий символ к строке
        s += arr[i]

        # добавляем последний символ к строке
    s += arr[len(arr) - 1]
    # если повторяющихся символов в строке нет
    if c == 0:
        # добавляем её в множество
        values.add(s)


# получаем перестановки
permutations = list(itertools.permutations(['К', 'А', 'П', 'К', 'А', 'Н']))
# перебираем их
for permutation in permutations:
    process_permutation(permutation)

# выводим размер множества
print(len(values))
