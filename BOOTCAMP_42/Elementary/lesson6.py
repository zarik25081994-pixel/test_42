a = int(input('Результаты по ЕГЭ:'))
russian = int(input("введите баллы по русскому языку: "))
math = int(input("введите баллы по математике: "))
informatics = int(input("введите баллы по информатике: "))
total = russian + math + informatics
if total >= 270:
    print('Поздравляю, ты поступил на бюджет')



w = int(input('Ves arbuza:'))
if w > 2 and w % 2 == 0:
    print ('yes')
else:
    print ('no')






a = 10
b = 5
if a > 0 and b > 0:
    print ('yes')

c = 10
g = 5
if c > g:
    print(c + 2)




mix = ['яблоко', 'картошка', 'лимон', 'помидор', 'шоколад', 'вишня', 'конфеты', 'дыня', 'абрикос', 'тыква', 'мармелад']
num1 = []
num2 = []
num3 = []
fruits = ['яблоко', 'лимон', 'вишня', 'дыня', 'абрикос']
sweets = ['шоколад', 'конфеты', 'мармелад']
vegetables = ['картошка', 'помидор', 'тыква']
num1.append('яблоко')
num1.append('лимон')
num1.append('вишня')
num1.append('дыня')
num1.append('абрикос')
print(num1)
num2.append('шоколад')
num2.append('конфеты')
num2.append('мармелад')
print(num2)
num3.append('картошка')
num3.append('помидор')
num3.append('тыква')
print(num3)



numbers = [1, -3, 5, -7, 9, -2]
plus = []
minus = []
plus.append(1)
plus.append(5)
plus.append(9)
print(plus)
minus.append(-3)
minus.append(-7)
minus.append(-2)
print(minus)


names = ['Akulya', 'Aigerim', 'Erbol', 'Aliya']
for name in names:
    if len(name) > 5:
        print(name)


numbers = [1, 2, 3, 4, 5 ]
for num in numbers:
    print(num)














menu = ['lagman-150 som', 'plov-300 som', 'borsh-105 som', 'manty-400 som : ']
menu.append('besh barmak-280 som')
print(menu)
menu.append('manty-310 som')
print(menu)
menu.remove('borsh-105 som')
print(menu)



a = [100, 200, 300, 400, 500, 600]
a.reverse()
print(a)


s = ['i', 'you', 'we', 'they :']
d = ['he', 'she', 'it :']
s.extend(d)
print(s)



names = ['Oskar', 'Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon', 'Jimmy', 'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jsckson', 'Jhon', 'Jack']
print(names.count('Jack'))
names.remove('Oskar')
print(names)


s = []
s.append('Zarina')
s.append(1994)
s.append('Python')
print(s)


pethonList = ['int', 'str', 'bool', 'if', 'else', 'elif', 'loop', 'tuple', 'None', True, False]
pethonList.pop(6)
print(pethonList)


f = ('Hello World')
print(f.split())



reference = 'Helper'
if reference == 'Helper':
    print('oh excellent')
elif reference == 2434 :
    print('ok')
else:
    print('mistake')


s = input('Your order : ')
if len(s) > 8:
    if s.isalpha():
        print('Exactly')

    if s == 'Hi my friend ' :
        print('yes')

    else:
        print( 'no')
else:
    print('is not')



a = [2, 4, 8, 9]
if 4 in a:
    a.remove(4)
    print(a)
    a.append(5)
    print(a)


if 'Lime' not in a:
    a.append('lime')
    print(a)















