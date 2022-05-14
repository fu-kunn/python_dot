initial_balance = int(input("Initial Balance? "))
# if initial_balance >= 100_000:
#     RATE = 1.1
# else:
#     RATE = 1.01
# RATE = 1.1 if initial_balance >= 100_000 else 1.01 
# 入力した値によって1.1または1.01の利率を表示している

match initial_balance:
    case n if n >= 100_000:
        RATE = 1.1
    case n if n >= 80_000:
        RATE = 1.08
    case n if n >= 60_000:
        RATE = 1.06    
    case _:
        RATE = 1.01

print(f"Curent rate: {RATE:.2f}")
print(f"Year 0: {initial_balance:,.2f}")
print(f"Year 1: {initial_balance * RATE:,.2f}")
print(f"Year 2: {initial_balance * RATE * RATE:,.2f}")