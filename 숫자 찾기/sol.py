def solution(num, k):
    new_str = str(num)
    for i in new_str:
        if i == k:
            return len(new_str[0:k])
        else:
            return -1