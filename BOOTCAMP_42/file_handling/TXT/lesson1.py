# a = open('txt', 'w', encoding='utf-8')
# a.write('Otkulbek kyzy \n\t\t\t Zarina \n\t\t\t\t\t age = 32 years old')
# a.close()
import csv
from fileinput import filename

from uaclient.files.notices import remove

# a = open('text.txt', 'w', encoding='utf-8')
# a.write('Have a lucky day !')
# a.close()


# s = open('day.txt', 'w', encoding='utf-8')
# s.write('Hi day, wish you \n\t\t\t\t many excellent things!')
# print(s.readline())
# s.close()

# s = open('day.txt', 'r', encoding='utf-8')
# print(s.read())
# print(s.readline())


# s = open('day.txt', 'r', encoding='utf-8')
# a = s.read()
# print(len(a))


# s = open('day.txt', 'r', encoding='utf-8')
# a = s.read()
# print(a.split())


# x = open('text.txt','w', encoding='utf-8')
# x.write('You are welcome!')
# x.close()


# s = open('txt.txt', 'w', encoding='utf-8')
# s.write('')
# s.close()

# b = open('day.txt', 'a', encoding = 'utf-8')
# b.write('\n\t\t\t\t\t this day is warm')
# b.close()


# d = open('day.txt', 'r', encoding='utf-8')
# # print(d.read())
# # print(d.readline())
# # f = d.read()
# # print(len(f))



# with open('day.txt', 'w', encoding='utf-8') as d:
#     lines = d.readlines()
# lines.sort()
# with open('sorted.txt', 'w', encoding='utf-8') as d:
#     d.writelines(lines)
#
#
#
#
#
# filenames = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']
# with open






# def my_file(filename):
#     with open(filename, 'w') as f:
#         f.write('hello world')
#
# my_file('Azim.txt')

# try:
#     with open ('zz.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
# except FileNotFoundError:
#     print('File not found')

# try:
#     with open('z.txt', 'x', encoding='utf-8') as f:
#         print(f.read())
# except FileExistsError:
#     print('File exists')


# def ff(filename):
#     with open(filename, 'w') as f:
#         f.write('hello')
#
# ff('a.txt')





# def moon(filename):
#     with open(filename, 'w') as f:
#         f.write('How much is this coat?')
#
# moon('price')




# try:
#     with open('tex.txt', 'r', encoding='utf-8') as f:
#         f.read()
# except FileNotFoundError:
#     print('There is no tex.txt')



# try:
#     with open ('z.txt', 'x', encoding='utf-8') as file:
#         print(file.read())
# except FileExistsError:
#     print('exist this file')






# def lll(keta):
#     with open('keta.txt', 'w', encoding='utf-8') as file:
#         file.write('Your visa is approved')
#
# lll('vis.txt')




# def kkk(visa):
#     with open(visa, 'w', encoding='utf-8') as f:
#         f.write('visa is approved')
#
# kkk('visa.txt')




# try:
#     with open('Azim.txt', 'w', encoding='utf-8') as f:
#         f.write('Hello Azim!')
# except FileNotFoundError:
#     print('no such file')




# def day(warm):
#     with open('monday.txt', 'w', encoding='utf-8') as f:
#         f.write('Today is so hot outside!')
#
# day('monday.txt')


# results = []
# less = []
# while True:
#     try:
#         a = int(input('Enter your age:'))
#         if a >= 18:
#             results.append(a)
#             print('You can enter!')
#         elif a < 18:
#             print('Unfortunately, you can not enter!')
#             less.append(a)
#     except ValueError:
#         print('Please enter a number!')
#
#     print(results)
#     print(less)







# import csv
# with open('students.csv', 'w', encoding='utf-8') as f:
#     w = csv.writer(f)
#     w.writerow(["Name", "Age"])
#     w.writerow(["Ali", "18"])
#     w.writerow(["Bob", "19"])
#     w.writerow(["Charlie", "20"])
#     w.writerow(["David", "21"])





# students = [
#     ['name', 'age', 'gender', 'city'],
#     ['Alihan', 14, 'male', 'Osh'],
#     ['Kamilla', 16, 'female', 'Bishkek']
# ]
# with open('students.csv', 'w', encoding='utf-8') as file:
#     w = csv.writer(file)
#     w.writerows(students)
#
# female = [
#     ['name', 'city']
# ]
# male = [
#     ['name', 'city']
# ]
# with open('students.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for i in reader:
#         if i[2] == 'female':
#             female.append(i)
#         elif i[2] == 'male':
#             male.append(i)
#
# print(female)
# print(male)
# with open('female.csv', 'w', newline= '', encoding='utf-8') as f:
#     w = csv.writer(f)
#     w.writerows(female)

























