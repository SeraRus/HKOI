from datetime import datetime

N = int(input())

week_list = ["Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"]
weekday = datetime(N, 2, 14).weekday()
weekday_text = week_list[weekday]
print(weekday_text)
