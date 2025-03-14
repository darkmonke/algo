def solution(num1, num2):
    answer = list()
    
    for i in str(num1 // num2 * 1000):
    answer += i

real_answer = answer[0:5]
    return real_answer

# What's wrong?

- // 연산자는 정수 나눗셈으로, 소숫점 이하를 버림. 따라서 나누기 연산 /를 사용해야 함.
- real_answer = answer[0:5]는 리스트의 앞 5개 요소만 선택함.