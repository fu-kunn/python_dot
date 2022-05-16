# for 回数が決まっている
# while 回数が決まっていない

command = int(input("Select 1, 2, 3 (0: Exit) "))
while command != 0:
    match command:
        case 1:
            print("Menu 1")
        case 2:
            print("Menu 2")
        case 3:
            print("Menu 3")
    command = int(input("Select 1, 2, 3 (0: Exit) "))        