def solution(n):
    answer = 0

    for i in range(1, n + 1, 2):
        answer += i

    return answer