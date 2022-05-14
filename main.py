# signal = input("Sgnal color? ")

# if signal == "red":
#     print("Stop")
# elif signal == "yellow":
#     print("Slow down")
# elif signal == "blue" or signal == "green":
#     print("Go")
# else:
#     print("Invalid signal color...")

# match
# Python 3.10~

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Slow down")
    case "blue" | "grenn":
        print("Go")
    case _:
        print("Invalid signal color...")