def solutuon(rsp):
    my_list = list(rsp)
    my_list[0] = 5
    my_list[2] = 0
    my_list[5] = 2

    answer = ''.join(my_list)
    return answer


# 단축평가란 논리 연산자(and, or)를 사용할 때, 첫 번째 피연산자의 값만으로 전체 표현식의 결과가 확정될 경우 두 번째 피연산자를 평가하지 않는 것을 말합니다.
# 단축평가의 원리

# 1. and 연산자:

# 첫 번째 피연산자가 False이면 두 번째 피연산자를 평가하지 않고 바로 False 반환
# 첫 번째 피연산자가 True이면 두 번째 피연산자의 값을 반환


# 2. or 연산자:

# 첫 번째 피연산자가 True이면 두 번째 피연산자를 평가하지 않고 바로 True 반환
# 첫 번째 피연산자가 False이면 두 번째 피연산자의 값을 반환