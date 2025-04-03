def solution(numbers):

    a = sorted(numbers, reverse=True)
    b = a[0] * a[1] 
    c = a[-1] * a[-2]

    if b >= c:
        return b
    else:
        return c 