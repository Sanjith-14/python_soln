import calendar

m, d, y = map(int, input().split())

date=calendar.weekday(y,m,d)

week=['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

print(week[date]);
