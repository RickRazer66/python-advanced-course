series_of_integers = input().split()

new_list = []
final_list = []
list_of_commands = []

command_data = list(map(str,input().split()))



while not command_data == "END":
    if command_data[0] == "add" and command_data[1] == "to" and command_data[2] == "start":
        final_list.extend(command_data[3:])
        final_list += series_of_integers
    elif command_data[0] == "add" and command_data[1] == "to" and command_data[2]=="end":
        pass
    elif command_data[0] == "remove" and command_data[1] == "greater" and command_data[2] == "than":
        pass
    elif command_data[0] == "replace":
        pass
    elif command_data[0] == "remove" and command_data[1] == "at" and command_data[2] == "index":
        pass
    elif command_data[0] == "remove" and command_data[1] == "count":
        pass
    elif command_data[0] == "find" and command_data[1] == "even":
        pass
    if command_data[0] == "find" and command_data[1] == "odd":
        pass



    command_data = input()
print(final_list)