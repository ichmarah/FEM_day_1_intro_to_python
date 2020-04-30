from datetime import datetime, timedelta

# Print today's date
today = datetime.now()
print(f'Today\'s date is {today}')

# timedelta() --> print previous dates without worrying about leap year
one_day = timedelta(days=1)
yesterday = today - one_day
print(f'Yesterday\'s date was {yesterday}')

seven_days = timedelta(days=7)
# You can use 'weeks' as well instead of the above code
one_week = timedelta(weeks=1)
last_week = today - seven_days
last_week2 = today - one_week
print(f'Last week\'s date was {last_week}')
print(f'Last week was {last_week2} – (using \'weeks=1\' in timedelta())')

# =====================================================

# Print current date in day, month, year
print(f'Day: {today.day}')
print(f'Month: {today.month}')
print(f'Year: {today.year}')

# =====================================================

# Print users input birthday
birthday = input('When is your birthday (dd/mm/yyyy)?')
# strp strips the elements form out of the string birthday and converts it into adatetime format
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
birth_year = birthday_date.year
# If user provides only two last digit in input(), there is a system error

# birthday_date = datetime.strptime(birthday, '%d/%m/%y') small letter 'y' gives only the last two digits of the birth year
print(f'Birthday: {birthday_date}\nBirth year: {birth_year}')
