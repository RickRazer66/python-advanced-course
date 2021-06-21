element = input()
element.split(", ")
list1 = []
start_index = 0

for i in range(0, len(list1)):
    list1[i] = int(list1[i])

for i in range(start_index, len(element)):
    if element == 0:
        list1.pop(element)
        list1.append(element)


print(list1)


