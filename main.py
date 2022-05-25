# タプル
# 要素を変更できない

tokyo = "JPY", 36, 140

tokyo = list(tokyo)
tokyo[0] = "YEN"
tokyo = tuple(tokyo)

print(tokyo)
print(tokyo[0])