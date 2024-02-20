import datetime

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
day, month, year = input().split(" ")
month = months.index(month) + 1
date = list(map(int, [year, month, day]))
expiryDate = datetime.date(*date)
expireDate = expiryDate + datetime.timedelta(days=int(input()))
print(f"{expireDate.day} {months[expireDate.month-1]} {expireDate.year}")
