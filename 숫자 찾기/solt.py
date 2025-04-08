def solution(num, k):
    num_str = str(num)
    k_str = str(k)
    
    if k_str in num_str:
        # 인덱스는 0부터 시작하므로 +1을 해서 자리 수로 변환
        return num_str.find(k_str) + 1
    else:
        return -1
    
    # find 함수는 찾을 문자 또는 찾을 문자열이 존재하는지 확인하고, 찾는 문자가 존재한다면 해당 위치의 index를 반환해주고, 찾는 문자가 존재하지 않는다면 -1을 반환