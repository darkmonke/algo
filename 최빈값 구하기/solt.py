def solution(array):
    # 각 숫자의 등장 횟수를 저장할 딕셔너리
    count_dict = {}
    
    # 배열 내 각 숫자의 등장 횟수 계산
    for num in array:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # 가장 많이 등장한 횟수 찾기
    max_count = max(count_dict.values())
    
    # 최빈값 찾기
    mode = [k for k, v in count_dict.items() if v == max_count]
    
    # 최빈값이 여러 개인 경우 -1 반환
    if len(mode) > 1:
        return -1
    
    # 최빈값이 하나인 경우 해당 값 반환
    return mode[0]

# 딕셔너리 쌍 추가 방법
a = {1: 'a'}
a[2] = 'b'
a
{1: 'a', 2: 'b'}
=> {1: 'a'} 딕셔너리에 a[2] = 'b'와 같이 입력하면 딕셔너리 a에 Key와 Value가 각각 2와 'b'인 {2: 'b'} 딕셔너리 쌍이 추가된다.