# открываем файл, относительный путь строится от папки со скриптом
# можно вместо этого закинуть файл куда-нибудь на диск и указать полный путь
with open('26-57.txt') as f:
    # читаем строку файла
    line = f.readline()
    # получаем элементы
    elems = line.split(' ')
    # кол-во кусков - первый элемент
    n = int(elems[0])
    # требуемая длину - второй
    m = int(elems[1])
    # создаём список длин кусков кабеля
    lst = []
    # читаем длины
    for i in range(n):
        lst.append(int(f.readline()))

    # сортируем длины
    lst.sort()

    # кол-во сварок
    sCnt = 0
    # кол-во оставшихся кусков
    rCnt = 0
    # пока в множестве есть элементы
    while len(lst) > 0:
        # сумма длин для нового блока
        sum = 0
        # кол-во использованных блоков
        eCnt = 0
        # пока суммарная длина меньше заданной и есть элементы в множестве
        while sum < m and len(lst) > 0:
            # получаем самый большой элемент множества, т.е. берём
            # кусок кабеля самой большой длины
            e = lst[-1]
            # убираем последний самый большой элемент из списка
            lst = lst[:-1]
            # добавляем его к суммарной длине
            sum += e
            # увеличиваем кол-во взятых кусков на 1
            eCnt = eCnt + 1

        # если в итоге сумма меньше требуемой длины,
        # значит, куски кабеля кончились, при этом их количество лежит в eCnt
        if sum < m:
            # просто сохраняем оставшееся количество
            rCnt = eCnt
            # завершаем цикл
            break
        # если суммарная длина больше или равна требуемой
        else:
            # получаем длину остатка
            nE = sum - m
            # добавляем его в множество
            lst.append(nE)
            lst.sort()
            # прибавляем к количеству сварок число сварок для этого блока
            # она на 1 меньшее числа кусков, ведь в сварке всегда участвует два блока
            sCnt += eCnt - 1

    # выводим кол-во сварных швов и кол-во оставшихся кусков
    print(sCnt, rCnt)