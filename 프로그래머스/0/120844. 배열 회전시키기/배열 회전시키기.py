def solution(numbers, direction):
    answer = []
    if(direction=="right"):
        answer+=[numbers[-1]]
        answer+= numbers[:len(numbers)-1]
    else:
        answer+= numbers[1:len(numbers)]  
        answer+=[numbers[0]]
    return answer