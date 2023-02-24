## Списки

numbers=[3,5,7,9,10.5]

print(numbers)

numbers.append('Python')

print(numbers)
print(len(numbers))

# Выведите на экран начальный элемент списка
print(numbers[0])

# Выведите на экран последний элемент списка
print(numbers[-1])

# Напечатайте элементы списка со второго по четвертый включительно
print(numbers[2:5])

#Удалите из списка строку "Python"
numbers.remove('Python')
print(numbers)
