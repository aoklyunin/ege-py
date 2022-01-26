# кол - во вершин графа
SIZE = 7

m = [
    [0, 5, 0, 12, 0, 0, 25],  # A
    [5, 0, 0, 8, 0, 0, 0],  # B
    [0, 0, 0, 2, 4, 5, 10],  # C
    [12, 8, 2, 0, 0, 0, 0],  # D
    [0, 0, 4, 0, 0, 0, 5],  # E
    [0, 0, 5, 0, 0, 0, 5],  # F
    [25, 0, 10, 0, 5, 5, 0],  # G
]


# поиск кратчайшего пути
def findMinDistance(start, end):
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
    print(findMinDistance(0, 6))
