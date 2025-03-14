1. 약수의 개수를 세기
2. 약수의 개수가 3개 이상이면 합성수(if)
3. 합성수의 개수를 세기

def solution(n):

    answer = []

for i in range(1, 101):
    if n % 2 != 0 and n % 3 != 0:
        answer += n

return answer.count + 2

# 리스트에 숫자를 추가할 때는 append 함수 사용(Line11)
# Line10에서 사용한 식은 n이 2와 3인 경우를 포함하지 않음. 이를 위해 'answer.count +2'를 했지만 해당 구문 또한 n이 2와 3인 경우를 포함하지 않음.