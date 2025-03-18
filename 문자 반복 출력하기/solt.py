def solution(my_string, n):
    answer = []
    for i in my_string:
        answer.append(i * n)
    return ''.join(answer)

# join 함수
# 정의: 리스트로 되어 있는 문자열 데이터들을 구분자(spectator)로 구분하여 문자열 형태로 반환하는 파이썬 내장 함수
# 형태: '구분자'.join(리스트)
# 주의사항: join 함수는 리스트 내 str형만 합칠 수 있음. 
# 만약 str형이 아닌 요소로 이루어진 list에 join 함수를 적용하려면 map 함수를 사용할 수 있음.
# ex) print(' '.join(map(str, List)))