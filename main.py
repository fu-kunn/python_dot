scores = [
  {"name": "Taro", "math":70, "english":82},
  {"name": "Jiro", "math":67, "english":61},
  {"name": "Saburo", "math":81, "english":58},
  ]

print("Name     Math      English")
print("-------- --------- --------")

for score in scores:
    for value in score.values():
        print(f"{value:8} ", end="")
    # print()のインデントに注意
    print()