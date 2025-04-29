num = [int(input()) for _ in range(10)]
numby=[i%42 for i in num]
print(len(set(numby)))