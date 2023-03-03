import datetime
x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2004, 12, 31)
print(x.strftime("%A"),"\n")

x = datetime.datetime.now()
print(x.strftime("%A")) #weekday full
print(x.strftime("%a")) #weekday short
print(x.strftime("%w")) #weekday as num
print(x.strftime("%d")) #day of month
print(x.strftime("%B")) #monthname full
print(x.strftime("%b")) #monthname short
print(x.strftime("%m")) #month as num
print(x.strftime("%Y")) #year full
print(x.strftime("%y")) #year short
print(x.strftime("%H")) #hour 00-23
print(x.strftime("%I")) #hour 00-12
print(x.strftime("%p")) #am/pm
print(x.strftime("%M")) #minute
print(x.strftime("%S")) #second
print(x.strftime("%f")) #microsecond
print(x.strftime("%z")) #UTC offset
print(x.strftime("%Z")) #Timezone: CST
print(x.strftime("%j")) #day num of the year
print(x.strftime("%U")) #week num of the year(1st day:Sunday)
print(x.strftime("%W")) #week num of the year(1st day:Monday)
print(x.strftime("%c")) #Local version of date and time
print(x.strftime("%C")) #Century
print(x.strftime("%x")) #local ver of date
print(x.strftime("%X")) #local ver of time
print(x.strftime("%%")) # '%'
print(x.strftime("%G")) #ISO 8601 year
print(x.strftime("%u")) #ISO weekday (1-7) 
print(x.strftime("%V")) #ISO weeknum (01-53)