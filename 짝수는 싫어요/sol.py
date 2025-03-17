def solution(n):
    if n % 2 == 0:
        return list(range(1, n, 2))
    elif n % 2 == 1:
        return list(range(1, n+1, 2))