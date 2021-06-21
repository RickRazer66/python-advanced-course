def check_password_is_valid(pword):
    is_valid = True
    count_digit = 0


    if len(pword) < 6 or len(pword) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False


    for el in pword:
        if el.isdigit():
            count_digit +=1


    if not pword.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False



    if count_digit < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


password = input()
result = check_password_is_valid(password)

if result:
    print("Password is valid")