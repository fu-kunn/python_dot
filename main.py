try:
    initial_balance = int(input("Initial Balance?" ))
except ValueError:
    print("Initial input, exiting...")
    exit()
RATE = 1.1
for year in range(3):
    print(f"Year {year}: {initial_balance * RATE ** year:,.2f}")