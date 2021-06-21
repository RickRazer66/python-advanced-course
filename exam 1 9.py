letters = input().split()
commands = input().split()

while not commands[0] == "Play":
    if commands[0] == "Move":
        index = intcommands[1]
        index_to_change = int(index)
        letters_as_string = letters
        if index_to_change not in range(letters):
            continue
        else:
            for letter in letters:
                letters[-1] = index_to_change
        if commands[0] == "Insert Space":
            index = commands[1]
            index_to_insert = int(index)
            letters.insert(index_to_insert, "")
        if commands[0] == "Exchange Tiles":
            pass
    commands[0] = input()

print(letters)