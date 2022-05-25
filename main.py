prices = [100, 200, 150, 200, 100]

# for price in prices:
#     print(price * 1.1)

# enumerate 関数
for index, price in enumerate(prices):
    print(f"{index}: {price * 1.1:.2f}")