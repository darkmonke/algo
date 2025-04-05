def solution(n):
    answer = []

    for i in range(1, n+1):
        answer.append('*' * i)
    for num in answer:
        print(num)

# python tutor에서는 정상적으로 출력되는데, 프로그래머스에서는 아웃풋 크기가 다르다고 나옴.