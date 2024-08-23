def solution(cipher, code):
    answer = ''
    j=0
    for i in cipher:
        j+=1
        if(j%code==0):
            answer+=i
            
            
            
            
    return answer