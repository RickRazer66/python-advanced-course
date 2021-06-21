username = input().split(", ")

SpecialSym =['$', '@', '#', '%', "^", "&", ":"]
valid_username = True

# while 3 < len()username) <16

for item in username:
    if item in SpecialSym:
        break
    if 3 < len(item) < 16:
        if item.isalnum() or "-" in item or "_" in item:
            print(item)

