import random

names = ["Taro", "Taro", "Taro", "Jiro", "Saburo", "Shiro", "Goro", ]

# random.shuffle(names)
# print(names)

# winner = random.choice(names)
# print(winner)

# winners = random.choices(names, k=3)
names = list(set(names))
winners = random.sample(names, 3)
print(winners)