def solution(n):
    sqrt = n ** 0.5
    if sqrt == int(sqrt):
        return 1
    else:
        return 2