def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])

# `str.isdigit`
# 숫자로만 구성된 문자열을 감지하는 함수
# 문자가 단 하나라도 있다면 False
# 모든 문자가 숫자로만 이루어져 있으면 True
# 마이너스, 소숫점은 뭇자로 판단하기 때문에 실수나 음수를 판단하지 못한다.