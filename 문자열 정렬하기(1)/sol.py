def solution(my_string):
    answer = []

    for i in my_string:
        if type(i) == int:
            answer.append(i)
    return answer.sort(reverse=False)

# 오류 발생 이유
# '배열의 유사도' 메모 참고
# my_string은 문자열이므로 for i in my_string:에서 i는 문자. 문자열에서 직접 가져온 문자는 문자열 형태이기 때문에 type(i) == int로 확인하면 항상 False가 됨.