# 真偽値
# True それ以外
# False 0 0.0 '' None

while True:
    command = int(input("Select 1, 2, 3 (0: Exit) "))
    match command:
        case 1:
            print("Menu 1")
        case 2:
            print("Menu 2")
        case 3:
            print("Menu 3")
        case 0:
            break
        case _:
            print("Invalid command, try again")
            continue
    print("Menu processed correctly")