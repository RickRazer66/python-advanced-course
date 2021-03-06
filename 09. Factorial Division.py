def calc_factorial(num):
    factorial = 1
    for n in range(1, num + 1):
        factorial *= n
    return factorial


def get_factorial_division(f1, f2):
    return f1 / f2


num1 = int(input())
num2 = int(input())
fact1 = calc_factorial(num1)
fact2 = calc_factorial(num2)
result = get_factorial_division(fact1, fact2)
print(f"{result:.2f}")
