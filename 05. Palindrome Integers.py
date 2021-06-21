def check_if_palindrome(el):
    if el == el[::-1]:
        return True
    return False


nums_as_string = input().split(", ")

for num_as_str in nums_as_string:
    is_palindrom = check_if_palindrome(num_as_str)
    if is_palindrom:
        print(True)
    else:
        print(False)