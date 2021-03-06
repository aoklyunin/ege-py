
import itertools
# кол-во вершин (используется для удобства)
SIZE = 7

# названия вершин
names = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж']

#   П1  П2  П3  П4  П5  П6  П7
source = [
    [0, 10, 15, 0, 0, 0, 0],  # П1
    [10, 0, 0, 13, 17, 0, 0],  # П2
    [15, 0, 0, 0, 19, 0, 9],  # П3
    [0, 14, 0, 0, 10, 20, 11],  # П4
    [0, 17, 19, 10, 0, 0, 20],  # П5
    [0, 0, 0, 20, 0, 0, 25],  # П6
    [0, 0, 9, 11, 20, 25, 0]  # П7
]
#    А  Б  В  Г  Д  Е  Ж
target = [
    [0, 1, 1, 0, 0, 0, 0],  # A
    [1, 0, 0, 1, 1, 0, 0],  # Б
    [1, 0, 0, 1, 0, 1, 0],  # В
    [0, 1, 1, 0, 1, 1, 0],  # Г
    [0, 1, 0, 1, 0, 1, 1],  # Д
    [0, 0, 1, 1, 1, 0, 1],  # Е
    [0, 0, 0, 0, 1, 1, 0]  # Ж
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
    print(arr)
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

    # расстояние между Г и Д
    gd_distance = source[arr[3]][arr[4]]
    # расстояние между Г и Е
    ge_distance = source[arr[3]][arr[5]]
    # расстояние между А и Б
    ab_distance = source[arr[0]][arr[1]]
    # если расстояние ГД меньше ГЕ, то комбинация нам подходит
    if gd_distance < ge_distance:
        # формируем заголовок
        header = ""
        # получаем обратную перестановку
        reverse = get_reverse_permutation(arr)
        for i in range(SIZE):
            header += names[reverse[i]] + " "
        # выводим названия вершин
        print(header)
        # выводим расстояния
        print(ab_distance, gd_distance, ge_distance)


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
