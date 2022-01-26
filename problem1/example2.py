
import itertools
# кол-во вершин (используется для удобства)
SIZE = 7

# названия вершин
names = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж']

#   П1  П2  П3  П4  П5  П6  П7
source = [
    [0, 11, 7, 5, 0, 0, 12],  # П1
    [11, 0, 0, 0, 13, 8, 14],  # П2
    [7, 0, 0, 15, 0, 10, 0],  # П3
    [5, 0, 15, 0, 0, 9, 0],  # П4
    [0, 13, 0, 0, 0, 6, 0],  # П5
    [0, 8, 10, 9, 6, 0, 0],  # П6
    [12, 14, 0, 0, 0, 0, 0]  # П7
]
#    А  Б  В  Г  Д  Е  Ж
target = [
    [0, 1, 0, 1, 0, 0, 0],  # A
    [1, 0, 1, 1, 0, 1, 0],  # Б
    [0, 1, 0, 0, 0, 1, 0],  # В
    [1, 1, 0, 0, 1, 0, 1],  # Г
    [0, 0, 0, 1, 0, 1, 1],  # Д
    [0, 1, 1, 0, 1, 0, 1],  # Е
    [0, 0, 0, 1, 1, 1, 0]  # Ж
]

# степени вершин
source_sum = [0 for i in range(SIZE)]
target_sum = [0 for i in range(SIZE)]

# поиск кратчайшего пути
def find_min_distance(start, end, arr):
    # заполняем расстояния от начальной вершины до рассматриваемой значениями -1
    distances = [-1] * SIZE
    # упорядоченное множество, в котором будут лежать индексы вершин графа, которые
    # начинаем с точки Б, поэтому индекс 1
    currentPoint = start
    # расстояние от точки до самой себя равно нулю
    distances[currentPoint] = 0
    # массив флагов, закончена ли проверка для заданной точки
    complete = [False] * SIZE
    # пока есть следующая точка
    while currentPoint != -1:
        # print("current: " , currentPoint, " " , names[currentPoint])
        # print(distances)
        # перебираем все вершины
        for i in range(SIZE):
            if i == currentPoint or complete[i]:
                continue
            # если у текущей есть с ней ребро
            if source[arr[currentPoint]][arr[i]] > 0:
                # если мы не обрабатывали вершину или новое расстояние через рассматриваемую вершину выше
                if distances[i] == -1 or distances[i] > distances[currentPoint] + source[arr[currentPoint]][arr[i]]:
                    # рассчитываем новое расстояние, как сумму длины пути до текущей вершины
                    # и ребра от текущей вершины до заданной
                    distances[i] = distances[currentPoint] + source[arr[currentPoint]][arr[i]]

        complete[currentPoint] = True
        # ищем следующую точку
        nextPoint = -1

        for i in range(SIZE):
            # если обработка точки не завершена
            if not complete[i]:
                # если мы уже доходили до точки и следующая точка ещё не задана или
                # новое расстояние меньше
                if distances[i] > 0 and (nextPoint == -1 or distances[i] < distances[nextPoint]):
                    nextPoint = i

        # переходим к следующей точке
        currentPoint = nextPoint

    return distances[end]


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
    minAGDistance = find_min_distance(0, 6, arr)
    # если расстояние ГД меньше ГЕ, то комбинация нам подходит
    if minAGDistance <= 15:
        # получаем обратную перестановку
        reverse = get_reverse_permutation(arr)
        out = ""
        # выводим названия вершин
        for i in range(SIZE):
            out += names[reverse[i]] + " "
        print(out)
        print(find_min_distance(4, 2, arr))


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
