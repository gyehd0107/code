def solution(my_string, num1, num2):
    
    listed = list(my_string)
    listed[num1],listed[num2]=listed[num2],listed[num1]
    answer=''.join(listed)
    return answer