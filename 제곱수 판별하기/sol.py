def solution(n):
    if type(n ** 0.5) == int:
        return 1
    else:
        return 2
# 위 코드에서 제곱근(n ** 0.5)이 정수여도 float 자료형으로 나올 수 있기 때문에 type() 함수를 사용하는 것은 적절하지 않음.