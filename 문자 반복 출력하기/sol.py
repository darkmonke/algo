def solution(my_string, n):
    
    answer = ''

    for i in my_string:
        while answer.count(i) < 6:
            answer.append(i)

    return answer