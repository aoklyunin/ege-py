# ход Пети, результат отвечает на вопрос, удовлетворяется ли
# требование задачи,  l - кол-во камней в первой куче, r - во второй,
# step - номер хода
def player1(l, r, step):
    # если это первый ход Пети, тогда Ваня пока что
    # не сделал ни одного хода
    if step == 1:
        # перебираем разные ходы Пети, нас устроит если хотя бы один
        # приведёт к выигрышу, поэтому используем ИЛИ
        # часть этих ходов может оказаться неудачной,
        # обработка этих ходов вернёт true
        # и в итоге приведёт к победе Вани
        return player2(l + 1, r, step) or player2(l, r + 1, step) \
               or player2(l * 2, r, step) or player2(l, r * 2, step)
    # если это второй ход Пети, Ваня ужк сделал первый ход
    else:
        # если сумма больше 77, то Ваня победил, условие
        # задачи выполнено
        return l + r >= 77


# ход Вани, результат отвечает на вопрос, удовлетворяется ли
# требование задачи второго хода Вани не предполагается, поэтому
# этот метод вызовется только для первого хода,
# l - кол-во камней в первой куче, r - во второй,  step - номер хода
def player2(l, r, step):
    # перебираем разные ходы Вани, нас устроит если хотя бы один
    # приведёт к выигрышу, поэтому используем ИЛИ
    return player1(l + 1, r, step + 1) or player1(l, r + 1, step + 1) \
           or player1(l * 2, r, step + 1) or player1(l, r * 2, step + 1)


# перебираем кол-во камней во второй куче
for s in range(1, 69 + 1):
    # запускаем обработку первого шага Пети, если
    # нас устраивает результат,
    if player1(7, s, 1):
        # выводим кол-во камней во второй куче
        print(s)
        # завершаем цикл
        break
