def get_price(a, b):
    if a + b >= 300:
        rate = 1.05
    total = (a + b) * rate #値が代入されていない変数→外のスコープを探す
    return total

# rate = 1.1
print(get_price(300, 700))
