def solution(numbers):
    answer = 0

    numbers.sort(reverse=True)

    return answer[-1] * numbers[-2]