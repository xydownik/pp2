from datetime import datetime
def difference(d1, d2):
  timedelta = d2 - d1
  return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2022-01-01 00:10:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()
print(difference(date1, date2))