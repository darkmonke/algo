def solution(num1, num2):
    answer = []
    
    for i in str(num1 // num2 * 1000):
        answer.append(i)

if '.' in answer:
    first_index = answer.index('.')
    real_answer = ''.join(answer[:first_index])
else:
    real_answer = ''.join(answer)

return int(real_answer)