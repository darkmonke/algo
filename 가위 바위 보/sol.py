def solution(rsp):
    answer = []

    for num in rsp:
        if num == 2:
            answer.append(0)
        elif num == 0:
            answer.append(5)
        elif num == 5:
            answer.append(2)
    return "".join(answer)