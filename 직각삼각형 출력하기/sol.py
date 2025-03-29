def solution(n):
    answer = []

    for i in range(1, n+1):
        answer.append('*' * i)
    for num in answer:
        return num