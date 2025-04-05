def solution(my_string):
    new_str = my_string.lower()
    return sorted(new_str)

    # sorted 함수는 리스트를 반환하기 때문에 문자열로 변환해야 함.