import itertools

# множество кодов
values = set()


# обработка перестановки
def process_permutation(arr):
    # переменная, которая отвечает на вопрос, подходит ли нам текущая комбинация
    # изначально кладём в неё ответ, правда ли, что первый символ - не 'Ь'
    f = arr[0] != 'Ь'
    # строка с кодом
    s = ""
    for i in range(len(arr) - 1):
        # если текущий символ - 'Ь', а следующий - гласная
        if arr[i] == 'Ь' and (arr[i + 1] == 'А' or arr[i + 1] == 'У'):
            # тогда комбинация нам не подходит
            f = False
        # прибавляем текущий символ к строке
        s += arr[i]

        # добавляем последний символ к строке
    s += arr[len(arr) - 1]
    # если повторяющихся символов в строке нет
    if f:
        # добавляем её в множество
        values.add(s)


# получаем перестановки
permutations = list(itertools.permutations(['В', 'У', 'А', 'Л', 'Ь']))
# перебираем их
for permutation in permutations:
    process_permutation(permutation)

# выводим размер множества
print(len(values))
