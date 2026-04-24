# people = {
#     'Nazik' : 120,
#     'Muslim': 100,
#     'Nuriza' : 85,
#     'Umar' : 80
# }
# s = [ ]
# x = [ ]
# for key, value in people.items():
#     if value >= 90 :
#         s.append(value)
#         print(s)
#     if value <= 90:
#         x.append(value)
#         print(x)
#


#
#
#
# movie = {
#     'film' : 'clone',
#     'year' : 2000,
#     'director' : 'Gloria_Peres',
#     'actresses': ['Govanna_Antonelly', 'Letissiya_Sabotello']
# }
# print(movie)

#
#
#
# vocabulary = {
#     'я' : 'I',
#     'ты' : 'you',
#     'мы' : 'we',
#     'они' : 'they',
#     'оно' : 'it'
# }
# for key, value in vocabulary.items():
#     print(key, value)
# words = input("Enter words in russian:")
# print(vocabulary.get(words))
#

#
#
# my_favourite = {
#     'town' : 'Rome',
#     'country' : 'Italy',
#     'population' : 200000000,
#     'sights': 'Collosseo'
# }
# for key, value in my_favourite.items():
#     print(key, ':', value)
# #
# #
# #
# city = {
#     'Italy':{'name': 'Rome', 'population': 200000000},
#     'Germany': {'name': 'Frankfurt', 'population': 250000000}
# }
# country = input('Enter a country name:')
# print(city.get(country,'Country dont found'))
# # #
# #
#



# weather = {
#     'monday': 10,
#     'tuesday': 12,
#     'wednesday': 14,
#     'thursday' : 16,
#     'friday': 11,
#     'saturday': 17,
#     'sunday': 19
# }
# for day, temperature in weather.items():
#     print(f'On {day} the temperature will be {temperature} ')
#     a = input('day:')
#     print(temperature)





# words = {
#     'summer': 6,
#     'winter': 6,
#     'spring': 6,
#     'fall': 4
# }
# for key, value in words.items():
#     print(key, value)
#     a = input('key:')
#     print(value)





#
#
#
# subjects = {'math' : 5, 'phisics': 4, 'chemistry': 3}
# for mark, mark2 in subjects.items():
#     if mark2 > 4:
#         print(mark)


#
# purchase = {'rice': 120, 'bread': 30, 'juice': 200}
# p = input('What do you want to buy? :')
# if p in purchase and purchase[p] > 0:
#     purchase[p] -= 1
#     print(purchase)

#
#
#
# prices = {'pasta': 300, 'wine': 500}
# general = 0
# while True:
#     a = input('Products:')
#     if a == 'thats all': break
#     if a in prices:
#         s = int(input('How much:'))
#         general += [a] * s
#         print('so:', general)

#
# menu = {'pasta': 600, 'artichokes': 500}
# s = { }
# total = 0
# while True:
#     portion = input('Meal:')
#     if portion == 'thats all': break
#     if portion in menu:
#         a = int(input('portions:'))
#         total += menu[portion] * a
# print('so:', total)

#
#
# vocabulary = { }
# while True:
#     key = input('keys:')
#     if key == 'thats all': break
#     value = input('values:')
#     # vocabulary[key] = value
#     # print(vocabulary)
#     vocabulary[value] = key
#     print(vocabulary)






# countries = {
#     'Italy': {
#         'capital': 'Rome',
#         'towns': ['Rome', 'Milan', 'Venice', 'Naples', 'Florence', 'Bologna'],
#         'population': 59000000,
#         'national food': ['pasta', 'pizza', 'lasagna', 'risotto'],
#         'culture': ['art', 'architecture', 'fashion', 'style'],
#
#     'Germany': {
#         'caital': 'Berlin',
#         'towns': ['Frakfurt am main', 'Humburg', 'Munich', 'Cologne', 'Stattgard'],
#         'population': 83500000,
#         'national food': ['pork knuckle', 'schnitzel', 'potatp salad' ],
#         'culture': ['art', 'literature', 'music', 'mentality'],
#     'Vatican': {
#         'capital': 'Vanican',
#         'towns': 'none',
#         'population': 1100 ['people'],
#         'national food': ['pasta', 'spaghetti'],
#         'culture': ['art', 'architecture', ' religion', 'language', 'education'],
#     'South Korea' : {
#         'capital': 'Seoul',
#         'towns': ['Seoul', 'Busan', 'Incheon', 'Daegu', 'Daejeon', 'Suwon'],
#         'population': 51000000,
#         'national food': ['kimchi', 'bulgogi', 'bibimbap'],
#         'culture': ['religion', 'kitchen', 'behavior'],
#     'Norway': {
#         'capital': 'Oslo',
#         'towns': ['Bergen', 'Trondheim', 'Stavanger', 'Drammen'],
#         'population': 5600000,
#         'national food': ['faricol', 'lutefisk', 'brunost', 'lefse'],
#         'culture': ['philosophy', 'Jantes law', 'home comfort'],
#     'Turkiye' : {
#         'capital': 'Ankara',
#         'towns': ['Istanbul', 'Antalya', 'Izmir', 'Adana'],
#         'population': 86000000,
#         'national food': ['kebab', 'kuru fasulye', 'dolma and sarma', 'corba'],
#         'culture': ['hospitality', 'respect for elders', 'religion' ],
#     'Luxembourg': {
#         'capital': 'Luxembourg city',
#         'towns': 'none',
#         'population': 682000 ['people'],
#         'national food': ['Judd mat Gaardebounen', 'bouneschlupp'],
#         'culture': ['multilingualism', 'festivals and dratitions', 'modisty and politeness'],
#     'Qatar': {
#         'capital': 'Doha',
#         'towns': ['Lusail', 'Al Vakra', 'Er Rayan', 'Um Salal'],
#         'population': 3000000,
#         'national food': ['machboos', 'waraka enab', 'harees'],
#         'culture': ['religion', 'falconry', 'sports and museums'],
#     'Portugal': {
#         'capital': 'Lisbon',
#         'towns': ['Porto', 'Braga', 'Amadora', 'Faru'],
#         'population': 10000000,
#         'national food': ['bakalhau', 'caldo verde', 'franzezinya'],
#         'culture': ['religion', 'football'],
#     'Spain': {
#         'capital': 'Madrid',
#         'towns': ['Barcelona', 'Valencia', 'Seville'],
#         'population': 48000000,
#         'national food': ['Paella', 'tapas' 'jamon'],
#         'culture': ['flamenco', 'football', 'architecture' ]}]
#
