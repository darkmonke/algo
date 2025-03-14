def solution(my_string):
    answer = 0

    numbers = []

    for char in my_string:
      if char.isdigit():
         numbers.append(int(char))

    return sum(numbers)