def solution(num1, num2):
    # num1을 num2로 나눈 후 1000을 곱하고 문자열로 변환
    result_str = str((num1 / num2) * 1000)
    
    # 소수점 위치 찾기
    if '.' in result_str:
        real_answer = result_str.split('.')[0]  # 소수점 앞부분만 추출
    else:
        real_answer = result_str
    
    return int(real_answer)

    # split 함수는 문자열을 특정 구분자(delimiter)를 기준으로 나누어 리스트로 만드는 문자열 메소드