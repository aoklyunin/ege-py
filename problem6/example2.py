# перебираем значения переменной i
for i in range(100000, 0, -1):
    d = i
    n = 0
    s = 0
    while s <= 365:
        s = s + d
        n = n + 5

    # если ответ совпал
    if n == 55:
        # выводим необходимое значение i
        print(i)
        # завершаем перебор
        break
