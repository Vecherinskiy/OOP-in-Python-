"""
Лабораторная работа 2 Задание 2

Свои классы из задания 1 перенёс в файл my_class
"""

from my_class import Dog, Car, Battery

if __name__ == "__main__":
    my_dog = Dog('Бобик', 5)
    my_car = Car('Audi', 'A7', 2019)
    my_battery = Battery(100, 10)
    try:
        my_dog.set_age(0)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        my_car.increment_odometer(-1)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        my_battery.charge_battery(-1)
    except ValueError:
        print('Ошибка: неправильные данные')
