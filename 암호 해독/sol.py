def solution(cipher, code):
    answer = []

    for i in range(1, 1001):
        answer.append(cipher[(code-1) * i])

    return ''.join(answer)