

# try:
#     while True:
#         print('Hi')
# except KeyboardInterrupt:
#         print('Произошла ручная остановка')




# at = 10
# nin = 15
# wo = 20
# for e in range(-at, at):
#     try:
#         print(wo / e)
#     except ZeroDivisionError:
#         print('Деление на ноль')
#     try:
#         if at > '5':
#             print('at > 5')
#     except TypeError:
#         print('Нельзя сравнивать число и строку')
#         if at > 5:
#             print( at > 5)

#
#
#
#
# lst = [ ]
# for i in range(10):
#     lst.append(i)
# try:
#     a = list(reversed(lst))
#     sls_obj = slice(0, 8)
#     print(a[sls_obj])
# except Exception as e:
#     print(f'Произошла непредвиденная ошибка : {e}')
#
#
#
#
#
# a = 0
# b = 1
# numbers = [ ]
# try:
#     while b > a:
#         numbers.append(b)
#         b += 1
#         if b > 10:
#             break
# except TypeError:
#     print('TypeError', 'chek that b is number, not a tuple')
# except Exception as e:
#     print(f'mistake: {e}')
# print(numbers)
#
#
#
#
#
# dict_ = {'name':'john', 'last_name': 'Snow', 12: 'age'}
# for x in dict_.keys():
#     try:
#         print(x + 'abc')
#     except TypeError:
#         print(f'impossible to plus to letters')
#     except Exception as e:
#         print(f'another mistake: {e}')
#
#
#
#
#
# data = {'name': 'John', 'age': 25}
# key = input('Enter a key:')
# result = data.get(key, 'key not found')
# print(result)






# try:
#     print('Zoo' + 15)
# except TypeError:
#     print('Нельзя складывать строку и цифры')







# at = 10
# nin = 15
# wo = 20
# try:
#     for e in range(-at, at):
#         print(wo / e)
# except ZeroDivisionError:
#         print('Division by zero')
# try:
#     if at > '5':
#         print(at > 5)
# except TypeError:
#     print('Нельзя сравнивать строку и цифры')








# lst = [ ]
# for i in range(10):
#     lst.append(i)
# print(lst)
# a = list(reversed(lst))
# sls_obj = slice(0, 8)
# print(a[sls_obj])





# a = (0)
# b = (1,)
# numbers = [ ]
# try:
#     while b > a:
#         print(b)
# except TypeError:
#     print('TypeError', 'chek that b is number, not a tuple')
# try:
#     numbers += b
#     print(b)
# except Exception:
#     print('Exception')
# try:
#     b += 1
#     print(b)
# except Exception:
#     print('Ex')

