# countries = {
#         'Italy': {
#         'capital': 'Rome',
#         'towns': ['Rome', 'Milan', 'Venice', 'Naples', 'Florence', 'Bologna'],
#         'population': 59000000,
#         'national food': ['pasta', 'pizza', 'lasagna', 'risotto'],
#         'culture': ['art', 'architecture', 'fashion', 'style'],
# },
#         'Germany': {
#         'capital': 'Berlin',
#         'towns': ['Frankfurt am Main', 'Hamburg', 'Munich', 'Cologne', 'Stattgard'],
#         'population': 83500000,
#         'national food': ['pork knuckle', 'schnitzel', 'potato salad' ],
#         'culture': ['art', 'literature', 'music', 'mentality'],
# },
#         'Vatican': {
#         'capital': 'Vatican',
#         'towns': 'none',
#         'population': 1100,
#         'national food': ['pasta', 'spaghetti'],
#         'culture': ['art', 'architecture', ' religion', 'language', 'education'],
# },
#         'South Korea' : {
#         'capital': 'Seoul',
#         'towns': ['Seoul', 'Busan', 'Incheon', 'Daegu', 'Daejeon', 'Suwon'],
#         'population': 51000000,
#         'national food': ['kimchi', 'bulgogi', 'bibimbap'],
#         'culture': ['religion', 'kitchen', 'behavior'],
# },
#         'Norway': {
#         'capital': 'Oslo',
#         'towns': ['Bergen', 'Trondheim', 'Stavanger', 'Drammen'],
#         'population': 5600000,
#         'national food': ['farical', 'lutefisk', 'brunost', 'lefse'],
#         'culture': ['philosophy', 'Jantes law', 'home comfort'],
# },
#         'Turkiye' : {
#         'capital': 'Ankara',
#         'towns': ['Istanbul', 'Antalya', 'Izmir', 'Adana'],
#         'population': 86000000,
#         'national food': ['kebab', 'kuru fasulye', 'dolma and sarma', 'corba'],
#         'culture': ['hospitality', 'respect for elders', 'religion' ],
# },
#         'Luxembourg': {
#         'capital': 'Luxembourg city',
#         'towns': 'none',
#         'population': 682000,
#         'national food': ['Judd mat Gaardebounen', 'bouneschlupp'],
#         'culture': ['multilingualism', 'festivals and dratitions', 'modisty and politeness'],
# },
#         'Qatar': {
#         'capital': 'Doha',
#         'towns': ['Lusail', 'Al Vakra', 'Er Rayan', 'Um Salal'],
#         'population': 3000000,
#         'national food': ['machboos', 'waraka enab', 'harees'],
#         'culture': ['religion', 'falconry', 'sports and museums'],
# },
#         'Portugal': {
#         'capital': 'Lisbon',
#         'towns': ['Porto', 'Braga', 'Amadora', 'Faru'],
#         'population': 10000000,
#         'national food': ['bakalhau', 'caldo verde', 'franzezinya'],
#         'culture': ['religion', 'football'],
# },
#         'Spain': {
#         'capital': 'Madrid',
#         'towns': ['Barcelona', 'Valencia', 'Seville'],
#         'population': 48000000,
#         'national food': ['Paella', 'tapas' 'jamon'],
#         'culture': ['flamenco', 'football', 'architecture' ]
# }}
# a = input('Enter a country:')
# if a in countries:
#         print(f'Information about a country {a}:')
#         print(f'Capital: {countries[a]['capital']}')
#         print(f'Population: {countries[a]['population']}')
#         print(f'National food: {countries[a]['national food']}')
#         print(f'Culture: {countries[a]['culture']}')
#         print(f'Towns: {countries [a]['towns']}')
# else:
#         print('Unfortunately there is no such country.')
#


# Set()

# a = {12, 34, 56, 78}
# print(a)




# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# a = set(numbers)
# print(a)



# a = { 12, 34, 4, 12, 34, 4, 6, 78}
# g = { 12, 34, 78, 45, 67, 88}
# print(a.intersection(g))
# print(a.difference(g))




# fruits = {'apple', 'banana', 'orange'}
# f = {'apple', 'banana'}
# fruits.add('kiwi')
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.remove('pear')
# print(fruits)
# fruits.discard('peach')
# print(fruits)







# numbers = {1, 2, 3, 4, 5, 6}
# if 3 in numbers:
#         print('Число найдено')




# colors = {'red', 'blue', 'green'}
# if 'black' not in colors:
#         colors.add('black')
#         print(colors)



# numbers = {10, 20, 30, 40}
# a = int(input('Enter a number:'))
# if a in numbers:
#         print('Есть вo множестве')
# else:
#         print('Нет вo множестве')



# a = { }
# f = list(a)
# while True:
#         s = int(input('Enter a number:'))
#         if s == 0:
#                 print('Stop')
#                 break
#
#         if s != 0:
#                 f.append(s)
#                 g = set(f)
#                 print(g)
#














# s = { }
# q = list(s)
# while True:
#     a = int(input('Enter a number:'))
#     if a == 0:
#         print('stop!')
#         break
#
#     if a > 0:
#         q.append(a)
#         k = set(q)
#         print(k)





# a = { }
# s = list(a)
# while True:
#     d = int(input('Enter a number:'))
#     if d in s:
#         print('dont repeat')
#         g = set(s)
#         break
#
#     if d > 0:
#         s.append(d)
#     print(s)









# n = { }
# a = list(n)
# while True:
#     d = int(input('Enter a number:'))
#     if d in a:
#         print('Dont repeat')
#         f = set(a)
#         break
#     a.append(d)






# a = ['fjkdhfkd', 'hjfkjff', 'TYUUI', 'TYJHJK']
# print(len(a))


# a = 12.3
# s = int(a)
# print(type(s))


# b = 43647
# s = int(b)
# print(s)


# a = 13
# a = 12
# print(a + a)

# name = 'qqq'
# print(name.replace('qqq','fff'))

# name = 'za ri n a'
# print(name.split())

# a = 'ghgjkf', 'fjgkgfl'
# print(a[0].isalpha())
# print(a[1].isalpha())


# f = 'uyithkHJFD'
# print(f.lower())
#
# g = 'GHkDfJK'
# print(g.upper())
#
# f = 'fhfekgjJL:sdfgRhYJ'
# print(f.isalpha())
#
#
# j =  'jhgkekf32564328292'
# print(j.isdigit())
#
# g = 'hgkrjkg375683275[[[['
# print(g.isalnum())
#
#
# k = 'tryuryrtttytyyyy'
# print(k.count('t'))
#
# h = 'hello_human'
# print(h.replace('h', 'k'))
#
# f = 'table spoon'
# print(f.split())
# #
# k = 'gf hk l kd'
# print(k.index('h'))
# #
#
#
# k = 'kiko'
# print(k.join('baby'))
# print(len(k))
#
#
#
# j = input('Your age ?:')
# print(j)







# a = 10
# d = 2
# print(a * d)
# print(a - d)
# print(a / d)
# print(a // d)
# print(a % d)
#
#
# n = 12 == 12 and 35 < 45
# print(n)
#



# k = int(input('Your age:'))
# if k >= 18:
#     print('you can enter')
# elif k < 18:
#     print('stop!')
# print(k)


# d = input('What do you want to buy?')
# if(len(d)) > 10:
#     print('here it')
# elif(len(d)) < 10:
#     print('sorry')




# a = input('Your password:')
# if (len(a)) > 8:
#     if a.isalnum():
#         print('correct')
#     if a == 'hello':
#         print('yes')
#     else:
#         print('error')
# elif(len(a)) < 8:
#     print('password is short')
# else:
#     if a.isdigit():
#         print('no letters')


# s = ['fear', 'red', 12, 456, 'hot']
# a = [ ]
# # print(type(s))
# # s.append('dear')
# # s.remove(12)
# # s.reverse()
# s.pop(2)
# a.extend('queen')
# s.insert(3, 'queen')
# print(s)





# d = [12, 34, 56, 67]
# a = [ ]
# if 12 in d:
#     d.append(13)
#     print(d)
# if 1 not in d:
#     d.append(1)
#     print(d)
# if 12 in d:
#     a.extend([11])
#     print(a)




# q = [4556, 567448, 78]
# print(sum(q))


# n = 'Hello world'
# print(n[3:])
# print(n[3:6])
# print(n[:-1])
# print(n[-1])
# print(n[:-6])
# print(n[0:6])



# name = 'Azim'
# for a in range(11):
#     print(name)
# for b in name:
#     print(b)

# name = 'Miza'
# for c in name:
#     print('Hi', name)

# b = 'Azim'
# for a in b:
#     print(b, end='!')



# a = ['345', '333', '444', '666']
# for s in a:
#     print(s, end=' ')





# name = 'Zarina'
# for n in range(10):
#     print('Hi', name, n)
#     print(f'hi {name} / {n}')
#     print(f'{name} ! {'you are my best friend!'} - {n}')



# for i in range(1, 5):
#     for j in range(5):
#         print(f'{i} * {j} = {i * j}')


# n = 10
# a = 5
# while n > a:
#     print(f'hello {a}')
#     a += 2
#


# s = { }
# q = list(s)
# while True:
#     a = int(input('Enter a number:'))
#     if a == 0:
#         print('stop!')
#         break
#
#     if a > 0:
#         q.append(a)
#         k = set(q)
#         print(k)
#


# n = { }
# a = list(n)
# while True:
#     d = int(input('Enter a number:'))
#     if d in a:
#         print('Dont repeat')
#         f = set(a)
#         break
#     a.append(d)

# s = { }
# q = list(s)
# while True:
#     a = int(input('Enter a number:'))
#     if a == 0:
#         print('stop!')
#         break
#
#     if a > 0:
#         q.append(a)
#         k = set(q)
#         print(k)



# f = { }
# s = list(f)
# while True:
#     a = int(input('Enter a number:'))
#     if a == 1:
#         print('stop')
#         break
#
#     s.append(a)
#     k = set(s)
#     print(k)



# a = int(input('Enter a number:'))
# d = int(input('Enter a number:'))
# g = input('Enter symbols:')
# if 2 + 2:
#     print(4)



# bulls = 10000
# cows = 5000
# cow = 1000
# total = 100000
# if total // bulls:
#     print(100000 // 10000)
# if total // cows:
#     print(100000 // 5000)
# if total // cow:
#     print(100000 // 1000)
#





# a = (13, 345, 333, 355)
# s = list(a)
# print(s)
# s.pop(3)
# print(s)
# d = tuple(s)
# print(d)
# print(type(d))


# d = ('ready', 12344, 89957)
# print(d.count(12344))
# print(d[2])



# a = { 1: 'one', 2: 'two', 3 :'three'}
# # # print(a.values())
# # # print(a.keys())
# # # print(a.items())
# print(a.update({'city':'bishkek'}))
# # print(a.popitem())
# # print(a.setdefault(5,'five'))
# # print(a.get(1))
# # print(a.pop(2))
# # print(a.items())
# a.update({'city': 'bish'})
# print(a.setdefault(4, 'four'))




# countries = {
#     'KZ': 'Bishkek',
#     'Korea': 'Seoul',
#     'india':'New_Deli'
# }
# a = input('Enter a country:')
# if a in countries:
#     # print(f'info about a country: {a}:')
#     # print(f'key: {countries[a]} city')
#     print(f'info about a country: {a}')
#     print(f'key: {countries[a]} city')




# a = {123}
# s = {12}
# print(a)
# print(type(a))
# print(a.add(4))
# print(a.pop())
# print(a & s )




# a = {12, 34, 56, 78, 89}
# s = {345, 5, 67, 78}
# print(type(a))
# print(a.pop)
# print(a.add(22))
# print(a.remove(12))
# print(a.discard(23))
# print(a.intersection(s))
# print(a.difference(s))








# def start():
#     s = input('Enter:')
#     if s == 'Start':
#         name = input('Your name:')
#         print(f'Hello, {name} ! welcome')
# start()




# def day():
#     for day in range(1, 6):
#         print(day, 'Hello')
# day()



# f = { }
# s = list(f)
# while True:
#     a = int(input('Enter a number:'))
#     if a == 1:
#         print('stop')
#         break
#
#     s.append(a)
#     k = set(s)
#     print(k)


# s = { }
# q = list(s)
# while True:
#     a = int(input('Enter a number:'))
#     if a == 0:
#         print('stop!')
#         break
#
#     if a > 0:
#         q.append(a)
#         k = set(q)
#         print(k)



# rooms = { }
# s = list(rooms)
# while True:
#     a = int(input('Enter a number:'))
#     if a >= 18:
#         print('Исключаем')
#         break
#
#     if a  < 18:
#         s.append(a)
#         k = set(s)
#         print(k)




# x = 10
# y = 10 * 10
# print(x + y)


# a = float (input('Enter the first number :'))
# d = float (input('Enter the second number :'))
# g = input('Enter symbol '+' :')
# if g == '+':
#         print(f'result: {a + d}')
# elif g == '-':
#         print(f'result: {a - d}')
# elif g == '*':
#         print(f' result: {a * d}')
# elif g == '/':
#     if d != 0:
#         print(f'result: {a / d}')
#     else:
#         print('wrong symbol')


# x = int (input('Enter X:'))
# y = int (input('Enter Y:'))
# day = 1
# while x < y:
#     x *= 1.1
#     day += 1
#
# print(day)
#



# total_money = 100000
# bull = 10000
# cow = 5000
# calf = 1000
#
# def decide():
#     for a in range(total_money // bull):
#         for b in range(total_money // cow):
#             for c in range(total_money // calf):
#                 if(a * bull + b * cow + c * calf ):
#                     return f'{a} {b} {c}'
# print(decide())












