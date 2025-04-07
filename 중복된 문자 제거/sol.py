핵심 아이디어

풀이 과정
1. my_string의 문자열 순서를 역전시킨다(my_string_rv).
2. for문을 이용해 반복해서 돈다.
3. 문자의 개수가 1개가 될 때까지 중복된 문자를 제거한다.
4. 다시 뒤집는다.

def solution(my_string): 

    my_string_rv = my_string[::-1]

    for i in my_string_rv:
        while my_string_rv.count(i) >= 2:
            my_string.replace(i, "")
            if my_string_rv.count(i) ==1:
                break
    return my_string_rv[::-1]