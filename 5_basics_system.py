import sys

# python version
print('Python version')
print(sys.version)
print('Version info.')
print(sys.version_info)


# print doc of built-in function (e.g. abs())
print(abs.__doc__)
print('\n')


# calendar of given month and year
import calendar
year = int(input('Input the year: '))
month = int(input('Input the month: '))
print(calendar.month(year, month))




