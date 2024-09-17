n, m=map(int, input().split())
K = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    x = j - i + 1
    for _ in range(x//2):
        temp = K[i-1]
        K[i-1] = K[j-1]
        K[j-1] = temp
        i += 1
        j -= 1

for o in K:
    print(o, end=' ')