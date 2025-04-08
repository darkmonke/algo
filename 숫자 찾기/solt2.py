def solution(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1
    return -1

# enumerate()는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력받았을 때, 인덱스와 값을 포함하여 리턴하는 함수