def solution(my_string):
    answer = ''
    collection=("a,e,i,o,u")
    for i in my_string:
        if(i not in collection):
            answer+=i
    
    return answer