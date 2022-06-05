import datetime


birthday = datetime.datetime(year=2000, month=4, day=11)
# print(birthday.year)
# print(birthday.month)
# print(birthday.day)
# print(birthday.minute)
# print(birthday.weekday()) #Mon;0, Tue:1....
birthday_formatted = birthday.strftime("%B %d %A, %Y")
print(birthday_formatted)