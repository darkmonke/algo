핵심 아이디어: 두 문자열의 길이와 각 문자의 개수가 동일해야 함.

def solution(before, after):

    if sorted(before) == sorted(after):
        return 1
    else:
        return 0