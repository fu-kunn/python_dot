def get_price(a, b):
    total = (a + b) * rate #値が代入されていない変数→外のスコープ
    return total
    
rate = 1.1
print(get_price(300, 700))
