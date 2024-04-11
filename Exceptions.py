import datetime

year, month, day = list(map(int, input().split()))
days = int(input().split()[0])

date = datetime.date(year, month, day)
delta = datetime.timedelta(days)

newdate = date+delta
print(newdate.year, newdate.month, newdate.day)