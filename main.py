# scores = [62, 91, 88]

scores = {"math":62, "english":91, "physics":88}

# scores["math"] = 100
scores["chemistry"] = 40
# del scores["english"]
popped_value = scores.pop("english")

print(scores)
# print(scores["english"])
print(popped_value)