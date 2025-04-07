핵심 아이디어

풀이 과정
1. my_string의 문자열 순서를 역전시킨다(my_string_rv).
2. for문을 이용해 반복해서 돈다.
3. 문자의 개수가 1개가 될 때까지 중복된 문자를 제거한다.
4. 다시 뒤집는다.

def solution(my_string): 

    my_string_rv = my_string[::-1]

    for i in my_string_rv:
        if my_string_rv.count(i) >= 2:
            my_string_rv.replace(i, "")
        elif my_string_rv.count(i) == 1:
            return my_string_rv[::-1]

# 오류 이유
# 파이썬에서 문자열은 불변(immutable). 즉 `my_string.replace(i, "")`는 원본 문자열을 수정하지 않고 새로운 문자열을 반환하는데, 위 코드에서는 이 결과를 저장하지 않음.