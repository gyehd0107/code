def solution(numbers):
    max=-10000*10000
        
    for i in  range(0,len(numbers)):
        for j in  range(1,len(numbers)):
            if(i!=j):
                r = numbers[i] * numbers[j]
                if(max<=r):
                    max= r
            

    answer=max
    return answer