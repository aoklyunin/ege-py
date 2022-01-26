# кол-во вершин (используется для удобства)
SIZE = 6

#   П1  П2  П3  П4  П5  П6  П7
m = [
    [0, 2, 4, 8, 0, 16],  # A
    [2, 0, 0, 3, 0, 0],  # B
    [4, 0, 0, 3, 0, 0],  # C
    [8, 3, 3, 0, 5, 3],  # D
    [0, 0, 0, 5, 0, 5],  # E
    [16, 0, 0, 3, 5, 0]  # F
]


def findMinDistance(start, end, skipPoint):
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
            if i == currentPoint or complete[i] or i == skipPoint:
                continue
            # если у текущей есть с ней ребро
            if m[currentPoint][i] > 0:
                # если мы не обрабатывали вершину или новое расстояние через рассматриваемую вершину выше
                if distances[i] == -1 or distances[i] > distances[currentPoint] + m[currentPoint][i]:
                    # рассчитываем новое расстояние, как сумму длины пути до текущей вершины
                    # и ребра от текущей вершины до заданной
                    distances[i] = distances[currentPoint] + m[currentPoint][i]

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


# главный метод программы
if __name__ == '__main__':
    part1 = findMinDistance(0, 4, 1)
    part2 = findMinDistance(4, 5, 1)
    print(part1 + part2)
