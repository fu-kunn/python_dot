scores = [
  {"name": "Taro", "math":70, "english":82},
  {"name": "Jiro", "math":67, "english":61},
  {"name": "Saburo", "math":81, "english":58},
  ]

print("Name     Math      English")
print("-------- --------- --------")

# def compare(score):
#     return score["math"]

# scores.sort(key=compare, reverse=True)
scores.sort(key=lambda score: score["math"], reverse=True)

for score in scores:
    for value in score.values():
        print(f"{value:8} ", end="")
    # print()のインデントに注意
    print()