def solution(my_string):
    answer = []

    for char in my_string:
        if char.isdigit():  # 문자가 숫자인지 확인
            answer.append(int(char))  # 숫자로 변환하여 추가

    return sorted(answer)  # 오름차순 정렬