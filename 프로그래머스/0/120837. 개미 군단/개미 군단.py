def solution(hp):
    answer = 0 
    s1=hp//5 
    s2=(hp-(s1*5))//3 
    s3=(hp-((s1*5)+(s2*3)))//1
    
    answer=(s2+s1+s3)
    
    return answer