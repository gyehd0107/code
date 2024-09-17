N=int(input())

arr=list(map(int, input().split()))
r_arr=[]
for i in range(N):
    numax=max(arr)
    r_arr.append((arr[i]/numax)*100)

avg_sum=sum(r_arr)
r_avg= avg_sum/N
print(r_avg)