# import datetime
#
# from module import lesson1
from datetime import datetime
from datetime import datetime
from datetime import datetime
# from datetime import datetime
from datetime import date , timedelta
import calendar
from datetime import date
from datetime import date
# from datetime import datetime
# from datetime import datetime
from datetime import date



# def next_monday():
#     today = datetime.today()
# date_now = datetime.datetime.now()
# hour = date_now.hour
#
# if hour < 12:
#     print('Good Morning!')
# elif 12 <= hour < 18:
#     print('Good Afternoon!')
# elif 18 <= hour < 22:
#     print('Good Evening!')
# else:
#     print('Good Night!')





# birthday = datetime(2026, 8, 25)
# now = datetime.now()
# delta = birthday - now
# days = delta.days
# total_seconds = int(delta.total_seconds())
#
# hours = (total_seconds // 3600) % 24
# minutes = (total_seconds // 60) % 60
# seconds = (total_seconds % 60) % 60
# print(f'Until my birthday:')
# print(f'days: {days}, hours: {hours}, minutes: {minutes}, seconds: {seconds}')
#










# birthday = datetime(2015, 3, 3)
# now = datetime.now()
# delta = now - birthday
# print(f'you have already lived: {delta.days} days')
#
#
#
#
#
# birth = datetime(1964, 1, 21)
# now =  datetime.today()
# delta = now - birth
# print(f'You have already lived: {delta.days}')
#







# def get_age(y):
#     today = datetime.today()
#     return today.year - y
#
# a = int(input('Enter a year:'))
# print(get_age(a))






# def next_monday():
#     today = date.today()
#     days_ahead = 0 - today.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return today + timedelta(days_ahead)
#
# print(f'Next monday: {next_monday()}')





# def get_mondays_next_month():
#     today = date.today()
#     year = today.year + (today.month // 12)
#     month = (today.month % 12) + 1
#     mondays = []
#     calendar = calendar.monthcalendar(year,month)
#     for week in calendar:
#         if week[calendar.MONDAY] != 0:
#             mondays.append(date(year, month, week[calendar.MONDAY]))
#             return mondays
#
# print(f'Mondays of month: {get_mondays_next_month()}')






# people = [
#     {'name': 'Lina', 'birthday': date(1990, 4, 14)},
#     {'name' : 'Azim', 'birthday': date(1995, 6, 20)}
# ]
# def chek_birthday(users):
#     today = date.today()
#     for user in users:
#         if user['birthday'].month == today.month and user['birthday'].day == today.day:
#             print(f'Today is birthday of: {user['name']}')
# chek_birthday(people)




# def free_date(target_date, busy_dates):
#     if target_date in busy_dates:
#         return 'date is busy'
#     return 'date is free'
#
# booked = ['2026, 4, 15', '2026, 4, 20']
# chek = '2026, 4, 14'
# print(free_date(chek, booked))








# now = datetime.now()
# formatted = now.strftime('%d, %m %Y, %H:%M:%S')
# print(formatted)



# a = datetime.strftime(date.today(), '%d-%m-%Y')
# print(a)





# s = date.today()
# a = datetime.isoweekday(s)
# print(a)
cd




