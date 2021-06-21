n = int(input())
stack = []

for index in range(n):
    commands = input().split()
    if commands[0] == "1":
        stack.append(int(commands[1]))
    elif commands[0] == "2":
        if len(stack) <= 0:
            pass
        else:
            stack.pop()
    elif commands[0] == "3":
        if len(stack) <= 0:
            pass
        else:
            print(max(stack))
    elif commands[0] == "4":
        if len(stack) <=0:
            pass
        else:
            print(min(stack))


reversed_numbers = []

for i in range(len(stack)):
    reversed_numbers.append(str(stack.pop()))

print(", ".join(reversed_numbers))