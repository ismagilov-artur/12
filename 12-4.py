a = input().split()
i, j = map(int, input().split())
answ = 0

for k in range(len(a)):
    if k >= i and k <= j:
        answ += int(a[k]) ** 2
print(answ)