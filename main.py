import calendar

#曜日を日曜日始まりにする
# calendar.setfirstweekday(6)
calendar.setfirstweekday(calendar.SUNDAY)

# cal_str = calendar.month(2001, 1)
# print(cal_str)

#データ型取得す場合
#週ごとの表示になっておりデータがない場合は「0」が表示される
# cal_date = calendar.monthcalendar(2001, 1)
# print(cal_date)

#閏年がある年をtrueかfalseで返す
print(calendar.isleap(2000))
print(calendar.isleap(2001))
