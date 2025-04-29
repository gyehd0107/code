num = [int(input()) for j in range(10)]
numby=[i%42 for i in num]
print(len(set(numby)))