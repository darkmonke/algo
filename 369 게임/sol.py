def solution(order):
    answer = 0
    new_str = '369'
    for i in new_str:
        answer = answer + str(order).count(i)
    return answer