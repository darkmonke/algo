def solution(array):
    answer = []

    for i in array:
        count = array.count(i)
        answer.append(count)

    a_dict = {
        'a': 3,
        'b': -1,
        'c': 1
        }

    return answer