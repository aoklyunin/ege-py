# открываем файл, относительный путь строится от папки со скриптом
# можно вместо этого закинуть файл куда-нибудь на диск и указать полный путь
f = open('27-1a.txt')

# читаем кол-во
n = int(f.readline())

# создаём массив для подсчёта подмножеств, сумма которых имеет тот
# или иной остаток от деления на 12
d = [0] * 12

# читаем сами числа
for i in range(n):
    # читаем число
    v = int(f.readline())
    # формируем новый массив остатков
    dc = d.copy()

    # Перебираем элементы нового массива остатков, т.к.
    # мы должны взять каждый из элементов массива остатков.
    # Кол-во чисел в нём говорит о том, сколько подмножеств имеют остаток
    # от деления суммы своих элементов. новый элемент мы можем добавить к любому
    # из подмножеств. Чтобы получить индекс полученного элемента, мы
    # просто находим остаток от деления суммы текущего остатка, равного i и
    # прочитанного числа. При этом т.к. мы могли взять любое из подмножеств с заданным остатком,
    # то надо прибавить кол-во этих множеств. Если мы не сделаем копию
    # массива, то часть остатков будет использовать уже изменённую сумму
    for j in range(12):
        dc[(v + j) % 12] += d[j]

    # также необходимо увеличить на 1 кол-во подмножеств, сумма элементов которых
    # будет иметь такой же остаток, как прочитанное число. Здесь мы
    # рассматриваем случай, когда новое подмножество состоит только из прочитанного элемента
    dc[v % 12] += 1
    # заменяем массив
    d = dc.copy()

# выводим кол-во подмножеств, имеющих сумму, делящуюся на 12, т.е имеющую
# остаток 0
print(d[0])
