# кол-во вершин (используется для удобства)
SIZE = 8

#   А  Б  В  Г  Д  Е  Ж  З
m = [
    [0, 5, 0, 2, 4, 0, 0, 0],  # А
    [0, 0, 0, 5, 0, 0, 7, 2],  # Б
    [0, 0, 0, 0, 0, 0, 0, 8],  # В
    [0, 0, 0, 0, 0, 0, 1, 0],  # Г
    [0, 0, 3, 0, 0, 0, 0, 0],  # Д
    [0, 0, 0, 0, 0, 0, 2, 0],  # Е
    [0, 0, 0, 0, 0, 0, 0, 0],  # Ж
    [0, 0, 0, 0, 0, 4, 0, 0],  # З
]

# названия вершин
names = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З']

# главный метод программы
if __name__ == '__main__':
    distances = [-1] * SIZE
    complete = [False] * SIZE
    currentPoint = 1
    # расстояние от точки до самой себя равно нулю
    distances[currentPoint] = 0
    # пока есть следующая точка
    while currentPoint != -1:
        # выводим расстояния
        print("current: ", currentPoint, " ", names[currentPoint])
        print(distances)
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

    # выводим расстояния
    print("current: ", currentPoint, " ", names[currentPoint])
    print(distances)
    # Выводим расстояние от Б до Ж
    print(distances[6])
