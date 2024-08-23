def solution(s1, s2):
    answer = 0
    cou=0
    if len(s1)>len(s2):
        l=s1
        l2=s2
    else:
        l=s2
        l2=s1
        
    for i in l:
        for j in l2:
            if(str(i)==str(j)):
                cou+=1
                
    answer=cou            
    return answer