# ход Пети, результат отвечает на вопрос, удовлетворяется ли
# требование задачи,
# s - кол-во камней в куче, step - номер хода
def player1(s, step):
    # если это первый ход Пети, тогда Ваня пока что
    # не сделал ни одного хода
    if step == 1:
        # выигрышная стратегия подразумевает, что
        # при любом поведении Вани требование  задачи должно быть удовлетворено,
        # если говорится, что тсратегия есть, значит,
        # нам подойдёт, если условие задачи выполнится в случае
        # хотя бы одного хода, поэтому используем ИЛИ
        return player2(s + 1, step) or player2(s + 4, step) or player2(s * 2, step)
    # если это второй ход Пети, т.е. Ваня сделал уже один ход
    else:
        # если Ваня при этом победил,
        if s >= 52:
            # требование задачи не выполнено
            return False

        # каким-то своим ходом Петя может выиграть,
        # то условие задачи будет выполнено, поэтому ИЛИ
        return player2(s + 1, step) or player2(s + 4, step) or player2(s * 2, step)


# ход Вани, результат отвечает на вопрос, удовлетворяется ли
# требование задачи,
# s - кол-во камней в куче, step - номер хода
def player2(s, step):
    # обработка состояния игры после хода Пети
    # если Петя сделал первый ход
    if step == 1:
        # если он при этом победил,
        if s >= 52:
            # требование задачи не выполнено
            return False

        # разные ходы Вани
        # нам нужно, чтобы при любом ходе Вани Петя победил, т.е.
        # требование задачи было выполнено, поэтому используем И
        return player1(s + 1, step + 1) and player1(s + 4, step + 1) and player1(s * 2, step + 1)
    # если Петя сделал второй ход
    else:
        # он должен победить
        return s >= 52


# проверка, может ли Петя выиграть первым ходом
def check(s):
    return s + 1 >= 52 or s + 4 >= 52 or s * 2 >= 52


# перебираем кол-во камней в куче
for s in range(1, 51 + 1):
    # запускаем обработку первого шага Пети, если
    # Петя не может выиграть за один ход и
    # Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня
    if not check(s) and player1(s, 1):
        # выводим кол-во камней во второй куче
        print(s)
