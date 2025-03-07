import math

def calculate(j,k):
    return math.factorial(j)/(math.factorial(k)*math.factorial(j-k))
T= int(input())

for _ in range(T):
    N,M = map(int, input().split())
    print(int(calculate(M,N)))