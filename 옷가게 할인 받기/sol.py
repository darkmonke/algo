def solution(price):
    if 100000 % price >= 100000:
        return 100000 * (1 - 100000 * 0.05)
    elif 300000 % price >= 300000:
        return 300000 % price * (1 - 300000 * 0.1)
    elif 500000 % price >= 500000:
        return 500000 % price * (1 - 500000 * 0.2)