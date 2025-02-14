def solution(n, k):
    answer = 0

    answer = (n * 12,000) + (k * 2,000) - (n//10 * 2,000)
    return answer