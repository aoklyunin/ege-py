import itertools

# кол-во вершин (используется для удобства)
SIZE = 7

# названия вершин
names = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'К']

#   П1  П2  П3  П4  П5  П6  П7
source = [
            [0, 45, 0, 10, 0, 0, 0], # П1
            [45, 0, 0, 40, 0, 55, 0], # П2
            [0, 0, 0, 0,15, 60, 0], # П3
            [10, 40, 0, 0, 0, 20, 35], # П4
            [0, 0, 15, 0, 0, 55, 0], # П5
            [0, 55, 60, 20, 55, 0, 45], # П6
            [0, 0, 0, 35, 0, 45, 0]  # П7
]
#    А  Б  В  Г  Д  Е  К
target = [
            [0, 1, 1, 0, 0, 0, 0], # A
            [1, 0, 1, 0, 0, 0, 0], # Б
            [1, 1, 0, 1, 1, 1, 0], # В
            [0, 0, 1, 0, 0, 1, 1], # Г
            [0, 0, 1, 0, 0, 1, 0], # Д
            [0, 0, 1, 1, 1, 0, 1], # Е
            [0, 0, 0, 1, 0, 1, 0]  # К
]

# степени вершин
source_sum = [0 for i in range(SIZE)]
target_sum = [0 for i in range(SIZE)]


# получить обратную перестановку
def get_reverse_permutation(arr):
    reverse = [0] * len(arr)
    for i in range(len(arr)):
        reverse[arr[i]] = i

    return reverse


# обработка перестановки
def process_permutation(arr):
    # проверяем, что в представлениях совпадают степени вершин
    for i in range(SIZE):
        if source_sum[arr[i]] != target_sum[i]:
            return

    # нужна проверка связности, т.е. того, что при перестановке все связи сохраняются, те не
    # обратятся в ноль
    for i in range(SIZE):
        for j in range(SIZE):
            # если в эталонном представлении связь между вершинами есть,
            # а в данном в задании - нет
            if target[i][j] > 0 and source[arr[i]][arr[j]] == 0:
                # заканчиваем выполнение обработчика, потому такая перестановка
                # создаёт представление, не совместимое с данным, а значит, нас не
                # интересует
                return

    # здесь мы уже выполняем проверку, определённую заданием

    # формируем заголовок
    header = ""
    # получаем обратную перестановку
    reverse = get_reverse_permutation(arr)
    for i in range(SIZE):
        header += names[reverse[i]] + " "

    # выводим названия вершин
    print(header)
    veDistance = source[arr[2]][arr[5]]
    print(veDistance)


# главный метод программы
if __name__ == '__main__':
    # рассчитываем взвешенные степени
    for i in range(SIZE):
        source_sum[i] = 0
        target_sum[i] = 0
        for j in range(SIZE):
            # в исходном представлении надо не забыть заменить ненулевые веса единицей
            source_sum[i] += 1 if source[i][j] > 0 else 0
            target_sum[i] += target[i][j]

    permutations = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6]))
    for permutation in permutations:
        process_permutation(permutation)
