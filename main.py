keys = ["math", "english", "physics"]
values = [62, 91, 84]

# scores = {}
# for item in zip(keys, values):
#     # print(item)
#     key, value = item
#     scores[key] = value

scores = {key: value for key, value in zip(keys, values)}

print(scores)