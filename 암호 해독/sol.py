def solution(cipher, code):

    answer = []

    for i in range(0, len(cipher)):
        if i % (code) == 0:
            answer.append(cipher[i])

    return ''.join(answer)