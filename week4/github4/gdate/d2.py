from datetime import date, timedelta
today = date.today()
yesterday  = today - timedelta(1)
tomorrow = today + timedelta(1)
print(yesterday, today,tomorrow, sep = "\n")