

# Определение параметров
#
# def info(name: str, salary = 5000):
#     a = input('Enter name:')
#     d = input('Enter salary:')
#     if d == '':
#         return f'{a} {salary} '
#
# print(info('a'))




#         Аннотация
#
#
# def names (a: str, s : str, d : int) -> list:
#     '''
#     Собирает данные о фильме в список.
#     :param a: movie
#     :param s: operator
#     :param d: year
#     :return: list
#     '''
#     return [a, s, d]
#
# print(names(a = 'vow', s = 'Jimm Carry', d = 2020))
#
#
#
#
# def lessons(a: str, s : int, d: int) -> list:
#     '''
#     Собирает данные об оценках в список.
#     :param a: lesson
#     :param s: mark
#     :param d: exam
#     :return: list
#     '''
#     return [a, s, d]
#
# print(lessons(a = 'math', s = 5, d = 4 ))
#
#
#
#
# def game(a: str, s: str, f : int) -> list:
#     '''
#     Собирает данные об игре в список.
#     :param a: run
#     :param s: catch ball
#     :param f: how many peoples
#     :return: list
#     '''
#     return [a, f, s]
#
# print(game(a = 'volleyball', s = 'goals', f = 12))
#
#
#
#
#
#
# def solo(a : str, s : int) -> list:
#     '''
#     Собирает данные о певце в список.
#     :param a: who sings
#     :param s: how many peoples
#     :return: list
#     '''
#     return [a,s]
#
# print(solo(a = 'man', s = 1))
#
#
#
#
#
#         *Args  Распаковка
#
#
# def plate(color, *args):
#     print(f'color: {color}')
#     print(f'Characteristic: {args} ')
#
# plate('black', 'round', 'with prints')
#
#
#
#
# def flowers(size, *args):
#     print(f'size: {size}')
#     print(f'price: {args} ')
#
# flowers('one meters', 1000)
#
#
#
# def flowers(size, *args, **kwargs):
#     print(f'size: {size}')
#     print(f'price: {args} ')
#
#     for key, value in kwargs.items():
#         print(f'{key} - {value}')
#
# flowers('one meters', 1000, adress='street Lenina, number 5', phone='050215452')
#
#
#
# a, b, *c = [4, 7, 8, 'hello', 77, 14]
# print(a, b, c)
#
#
#
# def f(a, b, c, d):
#     print(a, b, c, d)
#
# f(1, 2, 3, 4)
# l = ('hello', True, 78, [13, 4, 5])
#
# f(*l)
#
#
#
#
# def info(name: str, salary = 5000):
#     a = input('Enter your name:')
#     d = input('Enter your salary:')
#     if d == '':
#         print(f'{a} - {salary}')
#
#
#
#
#
# def games(name:str, participants:int, goals:int)-> list:
#     '''
#     Collect information about the game in tuple.
#     :param name: to run
#     :param participants: peoples
#     :param goals: win
#     :return: list
#     '''
#     return (name, participants, goals)
#
# print(games(name='football', participants= 22, goals=3))







