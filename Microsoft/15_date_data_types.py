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