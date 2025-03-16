def solution(array):
    new_array = array.sort()
    array_median = len(new_array) // 2
    return new_array[array_median]

    # 이 코드가 틀린 이유