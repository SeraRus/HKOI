import calendar

dateNum = int(input())


def switch_date(date_):
    date_ = date_.split(" ")
    date_[0] = int(date_[0][:-1])
    date_[1] = list(calendar.month_name).index(date_[1])
    date_[2] = int(date_[2])
    date_ = date_[::-1]
    return date_


dates = []
for i in range(dateNum):
    dates.append(switch_date(input()))
dates.sort()

for date in dates:
    formatted_date = "{}, {} {}".format(date[2], calendar.month_name[date[1]], date[0])
    print(formatted_date)
