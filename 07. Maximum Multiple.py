divisor = int(input())
bound = int(input())

n = 0

for number in range(1, bound + 1):
    if number % divisor == 0:
        n = number
print(n)
