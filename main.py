initial_balance = int(input("Initial Balance? "))
RATE = 1.1

# 1と2の時に+10000の処理を行う
for i in range(3):
    if i != 0:
        initial_balance += 10_000
    for year in range(3):
        print(f"Year {year}: {initial_balance * RATE ** year:,.2f}")
