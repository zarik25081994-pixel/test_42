# from selectors import SelectSelector
# from types import LambdaType
#
#                         # function Lambda
#

# add = lambda a, b : a + b
# print(add(12, 12))
#
#
#
#
#
# a = lambda x, y: x + y
# print(a(18, 12))
# #
#
#
#
# s =  lambda a, b, s : a - b -s
# print(s(100, 20, 30))
#
#
#
# d = lambda q, e, r : q * e * r
# print(d(8, 8, 8))
#
#
#
# g = lambda e, t, y: e / t / y
# print(g(100, 10, 2))
#
#
#
# a = lambda q : q * 2
# print(a(10))
#
#
#
# a = lambda number : 'True' if 10 % 2 == 0 else 'False'
# print(a('True'))
#
#
#
#
# s = lambda a, s : a + s
# print(s(16, 14))
#
#
#
# d = lambda q , w : 20, 18
# print(max(20, 18))
#
#
#
# d =  lambda a : 'True' if 20 % 5 == 0 else 'False'
# print(d('True'))
#
#
#
# a = 'we'
# if len(a) <= 3:
#     print('short')
# else:
#     print(False)
#
#
# a = lambda f: 'short' if len(f) <= 3  else 'long'
# print(a('we'))
#
#
#
#
# s = lambda d: 'True' if 'a' in d  else 'False'
# print(s(input('Enter a word:')))
#
#
#
#
#
# n = lambda students: 'it is all right' if students == 39 else 'wrong'
# print(n(39))
#
#
#
# try:
#     x = int(input('Enter a number:'))
#     x += 5
#     print(x)
# except ValueError:
#     print('better enter a letter:')
#
#
#
#
#
# x = 0
# while x == 0:
#     try:
#         x = int(input('Enter a number:'))
#         x += 5
#         print(x)
#     except ValueError:
#         print('better enter a number:')
#
#
#
#
# def lessons(*args, **kwargs):
#     if args == 40:
#         print('it is right')
#     if kwargs.get('name') == 'Liya':
#         print('Welcome Liya')
#
# lessons(40, name = 'Liya', age = 20)
#
#
#
# a = 15
# f = lambda a: 'Yes' if a == 15 else 'No'
# print(f(int(input('Enter a number:'))))
#
#
#
#
# a = lambda w, e, r, t: w + e - r - t
# print(a(5, 10, 5, 1))
#
#
#
#
#
# g = lambda k:'Azim' if k == 15 else 'nobody'
# print(g(15))
#
#
# d = lambda a: 'exactly' if a == 16 else 'wrong'
# print(d(int(input('Enter a number:'))))
#
#
#
#
#
# mistakes:
#
#
# syntax error:
# if a > 5
#     print(a)     (:)
#
#
# indentation error:
# def info():
# print('hi')   (отступ у принта)
#
#
# name error:
# print(a)    (переменная не была создана ранее)
#
#
#
# type error:
# print('5' + 1)  (нельзя складывать строку и число)
#
#
# zerodivision error:
# result = 1 / 0      (деление на ноль)
#
#
#
# keyerror:
# a = {'a': 2}
# print(a['c'])    (ключа б нет в словаре)
#
#
#
# indexerror:
# a = [1, 2, 3]
# print(a[4])     (индекс не в диапазоне, нет такого индекса)
#
#
#
#
#
# def lessons(*args, **kwargs):
#     if args == 10:
#         print('welcome')
#     if kwargs.get('name') =='Alla':
#         print('yes')
#
# lessons(10, name = 'Alla', age = 17)







# x = 0
# while x == 0:
#     try:
#         x = int(input('Enter a number:'))
#         x += 5
#         print(x)
#     except ValueError:
#         print('better enter a number:')





# a = 1
# while a == 1:
#     try:
#         a = int(input('Enter a number:'))
#         a += 5
#         print(a)
#     except ValueError:
#         print('better enter a number:')
#
#
#
#
#
# s = 2
# while s == 2:
#     try:
#         s = int(input('Enter a number:'))
#         s += 5
#         print(s)
#     except ValueError:
#         print('better enter a number:')



# def peoples(*args, **kwargs):
#     if args == 90:
#         print('it is okay')
#     if  kwargs.get('age') == 30:
#         print('welcome')
#
# peoples(90, age = 30, name = 'Alla')





# a = 1
# try:
#     s = int(input('Enter a number:'))
#     if s == 1:
#         print('It is true number!')
# except ValueError:
#     print('Better enter a number:')
# else:
#     print('it is true')
# finally:
#     print('Goodbye!')




# x = 0
# while x == 0:
#     try:
#         x = int(input('Enter a number:'))
#         x+= 5
#         print(x)
#     except ValueError:
#         print('better enter a number:')
#     except ZeroDivisionError:
#         print('can not device to zero')
#     else:
#         print('else')
#     finally:
#         print('Bye')





# a = 8
# while a == 8:
#     try:
#         s = int(input('Enter a number:'))
#         if s % 2 == 0:
#             print('correct')
#     except ValueError:
#         print('Incorrect input')
#     else:
#         print('wrong')
#     finally:
#         print('Goodbye')







#  syntax error:
# if a > 5
#     print(a)     (:)
#
# for i in n
#     print(i)
# #
#
# indentation error:
# def info():
# print('hi')
# #
# #
# if a  > 4:
# print(a)
# #
#
# name error:
# print(a)


# if a == 12:
#     a.append('Hi')
# print(a)



# type error:
# print('5' + 1)
#
# number = 12
# a = '12'
# print(a + number)
#
#

# zerodivision error:
# result = 1 / 0
#
# print(12 / 0)
# #
#
#
# keyerror:
# a = {'a': 2}
# print(a['c'])
#
#
# s = {'name': 'Lina', 'age': 15}
# print(s['town'])
# #
#
#
# indexerror:
# a = [1, 2, 3]
# print(a[4])
#
#
# s = [12, 34, 56]
# print(s[5])




# ValueError:

# a = input('Enter a number:')
# if s in a:
#     print('True')




# print(13 + 'Italy')








