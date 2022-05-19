def get_price(a, b):
    total = a + b #ローカル変数
    return total
    
total = 30 #グローバル変数
print(get_price(300, 700))
print(total)