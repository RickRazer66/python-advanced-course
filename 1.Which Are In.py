string = input()
commands_data = input().split()
action = commands_data[0]

while action == "Finish":
    if action == "Replace":
        letter_to_remove = commands_data[1]
        new_letter = commands_data[2]
        new_string = string.replace(letter_to_remove, new_letter)
    elif action == "Cut":
        start_index, second_index = int(commands_data[1]), int(commands_data[2])
        sub_string = string[start_index:second_index]
        for letter in range(len(string)):
            if letter not in sub_string:
                print(letter)
        break
    elif action == "Make":
        pass
    elif action == "Check":
        pass
    elif action == "Sum":
        pass


commands_data = input().split

print(new_string)