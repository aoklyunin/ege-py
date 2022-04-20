cnt = 0


def F(n):
    global cnt
    cnt = cnt + 1
    if n >= 1:
        cnt = cnt + 1
        F(n - 1)
        F(n - 2)
        F(n - 3)


F(22)
print(cnt)
