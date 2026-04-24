# from mako.compat import ArgSpec
#
# # * Args
#
#
# more = []
# less = []
# def marks(**kwargs):
#     for key, value in kwargs.items():
#         if value >=90:
#             more.append(value)
#         if value <= 90:
#             less.append(value)
#
# marks(Nazik= 100, Nuriza = 80, Bayaman = 80, Emirhan = 80, Umar= 90)
# print(more)
# print(less)
# #
#
#
# def print_words(*args):
#     return args
# #
# print(print_words('summer', 'winter', 'earn', 'calf'))
# #
#
#
#
#
# def sum_numbers(*args):
#     print(sum(args))
#
# sum_numbers(13, 23, 12)



#




# def introduce(**kwargs):
#     name = kwargs.get('name' '')
#     age = kwargs.get('age' '')
#     town = kwargs.get('town' '')
#     print(f'Hi! My name is {name}, i am {age} years old, i am from {town}')
#
# introduce(name='Alica', age='25 years old', town='Bishkek')




# def person_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
# person_info(name = 'Dinara', hobby= 'reading', pet= 'cat')

#
#
#
# def show_info(*args, **kwargs):
#     print('args:', args)
#     print('kwargs:')
#     for key, value in kwargs.items():
#         print(f'{key} = {value}')
#
# (show_info(1, 2, 3, name='Aibek', age=30))








# def total(func, args):
#     return func(*args)
# result = total(lambda a,s : a * s,  (12, 13))
# print(result)





# def moon (a, args):
#     return a (* args)
# so = moon(lambda q, w, e : q * w + e, (12, 12, 56))
# print(so)




