def solution(n):
    answer = 0
    for i in 'n':
        answer += int(i)
    return answer

# 위 코드가 틀린 이유
# n에 따옴표를 붙이면 숫자가 문자열로 형변환되지 않음. 이는 문자 'n'자체를 나타내는 문자열