
def solution(n):
    answer = 0
    sqrt=n**0.5
    if(sqrt.is_integer()):
        answer=1
    else:
        answer=2
    return answer