# кол-во вершин (используется для удобства)
SIZE = 7

# названия вершин
names = ['A', 'B', 'C', 'D', 'E', 'F', 'Z']

#   П1  П2  П3  П4  П5  П6  П7
m = [
    [0, 4, 6, 0, 0, 0, 30],  # A
    [0, 0, 3, 0, 0, 0, 0],  # B
    [0, 0, 0, 11, 0, 0, 27],  # C
    [0, 0, 0, 0, 4, 7, 10],  # D
    [0, 0, 0, 0, 0, 4, 8],  # E
    [0, 0, 0, 0, 5, 0, 2],  # F
    [29, 0, 0, 0, 0, 0, 0]  # Z
]

pathCnt = 0


# сгенерировать пути
def generate_paths(currentPoint, target, inPathPositions, stepCnt):
    global pathCnt
    # если мы дошли до целевой вершины
    if currentPoint == target:
        # шагов всегда меньше на 1, чем вершин в пути, поэтому сравниваем
        # пятью вместо шести
        if stepCnt >= 5:
            # инициализируем массив порядковых номеров вершин
            pointOrder = [-1] * SIZE
            # перебираем вершины
            for i in range(SIZE):
                # если порядковый номер вершины в пути задан
                if inPathPositions[i] != -1:
                    # порядковый номер вершины
                    pointOrder[inPathPositions[i]] = i

            # находим, сколько вершин мы использовали при построении пути
            realSize = SIZE
            for i in range(SIZE):
                if pointOrder[i] == -1:
                    realSize = i
                    break

            # находим длину пути
            pathLength = 0
            for i in range(realSize - 1):
                pathLength += m[pointOrder[i]][pointOrder[i + 1]]

            # выводим вершины, которые участвую в пути в порядке следования
            out = str(pathLength) + ": "
            for i in range(realSize):
                out += names[pointOrder[i]]

            print(out)
            # увеличиваем кол-во путей на 1
            pathCnt = pathCnt + 1

    else:  # иначе
        # перебираем все вершины
        for i in range(SIZE):
            # если порядковый номер вершины в пути ещё не задан
            # и между обрабатываемой вершиной и перебираемой есть ребро
            if inPathPositions[i] == -1 and m[currentPoint][i] > 0:
                # получаем копию порядковых номеров массива
                copyInPathPositions = inPathPositions.copy()
                # задаём порядковый номер для перебираемой вершины
                copyInPathPositions[i] = stepCnt + 1
                # генерируем путь через эту вершину
                generate_paths(i, target, copyInPathPositions, stepCnt + 1)


# главный метод программы
if __name__ == '__main__':
    # все вершины изначально не участвуют в пути
    inPathPositions = [-1] * SIZE
    # начальная точка A
    start = 0
    # конечная точка Z
    target = 6
    # текущая точка имеет нулевой порядковый индекс
    inPathPositions[start] = 0
    # ищем все пути между двумя точками
    generate_paths(start, target, inPathPositions, 0)
    # выводим ответ
    print("path cnt: ", pathCnt)
