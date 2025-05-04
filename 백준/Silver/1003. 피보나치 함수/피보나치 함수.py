T = int(input())
test_cases = [int(input()) for _ in range(T)]

max_n = max(test_cases)


count_0 = [0] * (max_n + 1)
count_1 = [0] * (max_n + 1)

count_0[0] = 1
count_1[0] = 0

if max_n >= 1:
    count_0[1] = 0
    count_1[1] = 1

for i in range(2, max_n + 1):
    count_0[i] = count_0[i-1] + count_0[i-2]
    count_1[i] = count_1[i-1] + count_1[i-2]

for n in test_cases:
    print(f"{count_0[n]} {count_1[n]}")