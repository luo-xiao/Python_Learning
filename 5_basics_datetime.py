import datetime

# current date and time
now = datetime.datetime.now()
print('Current date and time: ' + now.strftime('%Y-%m-%d %H:%M:%S') + '\n')


# calc num of days between two dates
d1 = datetime.date(2014, 7, 2)
d2 = datetime.date(2014, 7, 11)
days_in_between = abs(d2 - d1)
print(days_in_between.days)
print('\n')