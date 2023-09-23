century = int(input())
year = century * 100
days = int(year * 365.2422)
hour = days * 24
min = hour * 60
print(f'{century} centuries = {year} years = {days} days = {hour} hours = {min} minutes')
