def solution(numbers):
    my_tuple = tuple(numbers)
    answer = 2 * my_tuple
    return answer

    # 이 코드가 틀린 이유
    파이썬에서 'tuple * 정수'는 tuple을 반복하는 연산이지 각 원소에 정수를 곱하는 연산이 아님.
    ex. my_tuple = (1, 2, 3)
        result = 2 * my_tuple
        ==> 결과값은 (1, 2, 3, 1, 2, 3)