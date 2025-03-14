def solution(my_string):
    answer = 0

    numbers = '0123456789'
    for char in my_string:
        if char in numbers:
            answer += int(char)
            
    return answer