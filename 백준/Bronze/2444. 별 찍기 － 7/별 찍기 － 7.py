N=int(input())
for i in range(1, N + 1):
    print(' ' * (N-i) + '*' * i, end='')
    print('*' * (i-1))
for j in range(1, N):
    print(' ' * j + '*' * (N-j), end='')
    print('*' * (N-1-j))