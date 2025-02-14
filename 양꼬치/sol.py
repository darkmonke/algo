def solution(n, k):

    if n > 10:
        service = n // 10
        answer = n * 12,000 + (k - service) * 2,000
    else:
        answer = n * 12,000 + k * 2,000

    answer = 0
    return answer