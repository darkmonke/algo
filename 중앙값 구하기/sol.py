def solution(array):
    new_array = array.sorted()
    array_median = len(new_array) // 2
    return new_array[array_median]

    # 이 코드가 틀린 이유
    sort() 함수 안에 매개변수 넣어야 함.

    # 새로 알게 된 내용
    // 연산자는 정수 나눗셈 연산자로, 결과를 항상 정수로 내림함. 반면 일반적인 나눗셈 연산자 /는 소수점이 있는 결과를 도출할 수 있음.