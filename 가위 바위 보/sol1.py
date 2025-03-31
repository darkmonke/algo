def solution(rsp):
    
    answer = list(rsp)
    
    for num in rsp:
        while num == 2:
            answer.append(0)
        while num == 0:
            answer.append(5)
        while num == 5:
            answer.append(2)
    return ''.join(answer)