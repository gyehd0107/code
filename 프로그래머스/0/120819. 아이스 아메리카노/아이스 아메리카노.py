def solution(money):
    answer = []
    n=int(money/5500)
    pay=money-5500*n
    answer.append(n)
    answer.append(pay)
    return answer