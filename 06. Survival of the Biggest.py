numbers = input().split()
numbers_to_remove = int(input())
int_list = []

for i in numbers:
    int_list.append(int(i))
for j in range(numbers_to_remove):
    int_list.remove(min(int_list))
print(int_list)