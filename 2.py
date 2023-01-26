"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

seconds = int(input("Введите время в секундах: "))

minutes = seconds // 60
seconds %= 60
hours = minutes // 60
minutes %= 60

if hours > 99:
    print("Вы ввели слишком большое число, число часов не подходит под формат чч:мм:сс")
else:
    seconds_1 = seconds % 10
    seconds_10 = seconds // 10
    minutes_1 = minutes % 10
    minutes_10 = minutes // 10
    hours_1 = hours % 10
    hours_10 = hours // 10

    print(f'{hours_10}{hours_1}:{minutes_10}{minutes_1}:{seconds_10}{seconds_1}')