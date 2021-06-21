

def data_types(command, number):
    if command == "int":
        result = int(number) * 2
        print(result)
    elif command == "real":
        result = float(number) * 1.50
        print(f"{result:.2f}")
    elif command == "string":
        print(f"${number}$")

        return command, number


command_input = input()
num = input()

data_types(command_input, num)