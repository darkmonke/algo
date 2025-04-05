def solution(num_list):
    result = []
    for num in num_list:
            result.insert(0, num)
    
    return result

    # 위 insert() 함수의 의미는 0번 인덱스에 num을 삽입하라는 의미. 인덱스가 범위를 초과하면 맨 끝에 추가