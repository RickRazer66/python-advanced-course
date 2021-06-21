def subtract(sum_result, num_3):
    return sum_result - num_3


def sum_numbers(num_1, num_2):
    result1 = num_1 + num_2
    result2 = subtract(result1, num3)
    return result2


num1 = int(input())
num2 = int(input())
num3 = int(input())

final_result = sum_numbers(num1, num2)
print(final_result)
