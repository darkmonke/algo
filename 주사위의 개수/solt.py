def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n )
# 언패킹 방식 활용