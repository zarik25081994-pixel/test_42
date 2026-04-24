# import random
#
# numbers = random.randint(1, 20)
# while True:
#     person = int(input('Enter your number:'))
#     if person < numbers:
#         print('cold')
#     elif person > numbers:
#         print('warm')
#     else:
#         print('You win!')
#         break





import json
a = input('Enter book title: ', 'Enter book author :', 'Enter book year')


name = 'library.json'
def add_book(books):
        title = input('Enter book title: ')
        author = input('Enter book author: ')
        year = input('Enter book year:')
        if year.isdigit():
            print('Mistake: the year must be a number!')
            books.append({'title': title, 'author': author, 'year': year})
            print('The book has been added!')


def remove_book(books):
        title = input('\nEnter book title for delete :')
        print('The book has been removed!')
        print('The book with that title does not searched!')

def search_book(books):
        title = input('\nEnter book title for search :')
        if title not in books:
            print('The book has been found!')


