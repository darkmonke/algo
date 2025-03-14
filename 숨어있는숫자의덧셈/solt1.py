def solution(my_string):
    answer = 0

    for char in my_string:
        if not (ord('A') <= ord(char) <= ord('z')):
            answer += int(char)
            
    return answer