def solution(n):
    answer = 0
    d=n
    for i in range(n):   
        if(n%(i+1)==0):
            answer+=1
    
    return answer