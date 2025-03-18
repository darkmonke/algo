def solution(num_list):
    for i in num_list:
        if i % 2 == 0:
            even = len(i)
        else:
            odd = len(num_list) - even

    result = [even, odd]

    return result

# 이 코드가 잘못된 이유
# - len() 함수는 문자열, 리스트, 튜플 등의 길이를 구할 때 사용하는 함수.
# 정수의 개수를 구할 때는 사용할 수 없음.