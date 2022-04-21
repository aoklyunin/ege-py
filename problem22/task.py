x = int(input())
Q = 9
L = 0
while x >= Q:
    L = L + 1
    x = x - Q

M = x
if M < L:
    M = L
    L = x

print(L)
print(M)
