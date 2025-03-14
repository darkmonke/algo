def solution(numbers):
    
    n = len(numbers);

    for i in range(n):
        for j in range(0, n-i+1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

            print(i, j)

    return numbers[-1] * numbers[-2]

print(solution([1, 2, 3, 4, 5]))