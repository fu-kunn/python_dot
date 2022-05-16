initial_balance = int(input("Initial Balance? "))
RATE = 1.1
# yearは変数
for year in range(10):
    print(f"Year {year}: {initial_balance * RATE ** year:,.2f}")
    