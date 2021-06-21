n = int(input())

odd_numbers = set()
even_numbers = set()

for i in range(n):
    name = input()

    ascci_sum = 0
    for letter in name:
       ascci_sum += ord(letter)
    ascci_sum = ascci_sum // (i + 1)

    if ascci_sum % 2 == 0:
        even_numbers.add(ascci_sum)
    else:
        odd_numbers.add(ascci_sum)

even_sum = sum(even_numbers)
odd_sum = sum(odd_numbers)



if even_sum == odd_sum:
    result = odd_numbers.union(even_numbers)
elif even_sum > odd_sum:
    result =  odd_numbers.symmetric_difference(even_numbers)
elif even_sum < odd_sum:
    result = odd_numbers.difference(even_numbers)

print(", ".join([str(x) for x in result]))