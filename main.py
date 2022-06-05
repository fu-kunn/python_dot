import datetime


day1 = datetime.datetime(year=2000, month=4, day=11)
day2 = datetime.datetime(year=2001, month=1, day=1)

# diff = day2 - day1
# diff_seconds = diff.total_seconds()
# diff_days = diff_seconds / 60 / 60 / 24
# print(diff_seconds)
# print(diff_days)

delta = datetime.timedelta(days=3, hours=5)
day3 = day1 + delta
print(day3)