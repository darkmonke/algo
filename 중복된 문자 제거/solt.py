def solution(my_string):
    result = ""
    # 문자열의 각 문자를 순회하면서
    for char in my_string:
        # 만약 결과 문자열에 해당 문자가 아직 없다면 추가
        if char not in result:
            result += char
    return result