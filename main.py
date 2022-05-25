prices = [100, 200, 150, 200, 100]

# append リストの要素を追加する
prices_with_tax = []
for price in prices:
    prices_with_tax.append(price * 1.1)

prices_with_tax = [price * 1.1 for price in prices]    

print(prices_with_tax)