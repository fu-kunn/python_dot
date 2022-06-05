import datetime

# now = datetime.datetime.now()
# print(now)

# birthday = datetime.datetime(year=2000, month=4, day=11)
# 文字列から値を作る方法
birthday = datetime.datetime.strptime("2000-04-11", "%Y-%m-%d")
print(birthday)