from datetime import datetime, timedelta

# Print today's date
today = datetime.now()
print(f'Today\'s date is {today}')

# timedelta() --> print previous dates without worrying about leap year
one_day = timedelta(days=1)
yesterday = today - one_day
print(f'Yesterday\'s date was {yesterday}')

seven_days = timedelta(days=7)
last_week = today - seven_days
print(f'Last week\'s date is {last_week}')

#=====================================================

# Print current date in day, month, year
print(f'Day: {today.day}')
print(f'Month: {today.month}')
print(f'Year: {today.year}')

#=====================================================

#Print users input birthday
birthday = input('When is your birthday (dd/mm/yyyy)?')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y') # If user provides only two last digit in input(), there is a system error

#birthday_date = datetime.strptime(birthday, '%d/%m/%y') small letter 'y' gives only the last two digits of the birth year
print(f'Birthday: {str(birthday_date)}')