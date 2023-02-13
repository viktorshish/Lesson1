## Словари - Dictionary

#Задание 1
dict = {'city': 'Москва', 'temperature': '20'}
print(dict['city'])
dict['temperature'] = str(int(dict['temperature'])-5)
print(dict)

#Задание 2
print(dict.get('country', 'Россия'))
dict['date'] = '27.05.2019'
print(len(dict))