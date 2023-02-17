## Словари - Dictionary

#Задание 1
from rich import print
weather = {'city': 'Москва', 'temperature': '20'}
print(weather['city'])
weather['temperature'] = str(int(weather['temperature'])-5)
print(weather)

#Задание 2
print(weather.get('country', 'Россия'))
weather['date'] = '27.05.2019'
print(len(weather))
