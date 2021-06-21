

def smallest_number(a, b, c):
    smallest = 0
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    return smallest


num1 = int(input())
num2 = int(input())
num3 = int(input())


print(smallest_number(num1,num2,num3))


