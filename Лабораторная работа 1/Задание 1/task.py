"""Лабораторная работа 1 Задание 1"""

import doctest


class Dog:
    """Простая модель собаки"""

    def __init__(self, name: str, age: int = 1):
        """
        Создание и подготовка к работе объекта "Собака"

        :param name: Имя собаки
        :param age: Возраст собаки (age >= 1). Значение по умолчанию 1

        Примеры:
        >>> my_dog = Dog("Тузик", 2) # нициализация экземпляра класса
        """
        if not (isinstance(age, int)):
            raise TypeError("name должен иметь тип string")
        self.name = name
        if not (isinstance(age, int)):
            raise TypeError("age должен иметь тип integer")
        if age < 1:
            raise ValueError("age должен быть больше или равен 1")
        self.age = age

    def get_name(self) -> str:
        """
        Возвращает имя собаки

        Примеры:
        >>> my_dog = Dog("Тузик", 2)
        >>> dog_name = my_dog.get_name()
        """
        return self.name

    def get_age(self) -> int:
        """
        Возвращает возраст собаки

        Примеры:
        >>> my_dog = Dog("Тузик", 2)
        >>> dog_age = my_dog.get_age()
        """
        return self.age

    def rename(self, new_name: str) -> None:
        """
        Функуия позволяет изменить возраст собаки

        :param new_name: Нове имя
        :raise TypeError: Если тип введенного значения отличается от string,
        то возвращается ошибка.

        Примеры:
        >>> my_dog = Dog("Тузик", 2)
        >>> my_dog.rename("Барбос")
        """
        if not (isinstance(new_name, str)):
            raise TypeError("new_name должен иметь тип string")
        self.name = new_name

    def set_age(self, new_age: int = 1) -> None:
        """
        Функуия позволяет изменить возраст собаки

        :param new_age: Новый возраст
        :raise TypeError: Если тип введенного значения отличается от integer,
        то возвращается ошибка.
        :raise ValueError: Если введённое значение меньше 1, то возвращается ошибка.

        Примеры:
        >>> my_dog = Dog("Тузик", 2)
        >>> my_dog.set_age(5)
        """
        if not (isinstance(new_age, int)):
            raise TypeError("age должен иметь тип integer")
        if new_age < 1:
            raise ValueError("age должен быть больше или равен 1")
        self.age = new_age


class Car:
    """Простая модель автомобиля"""
    def __init__(self, manufacturer: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Машина"

        :param manufacturer: Производитель
        :param model: Модель
        :param year: Год выпуска

        Примеры:
        >>> my_car = Car("Audi", "A4", 2019) # инициализация экземпляра класса
        """
        self.manufacturer = manufacturer
        self.model = model
        if year < 1886:
            raise ValueError("Машин ещё не существовало, первая машина появилась в 1886")
        self.year = year
        self.odometer_reading = 0  # пробег машины

    def get_descriptive_name(self) -> str:
        """
        Возвращает описание автомобиля

        :return: Строка содержащая описание автомобиля

        Примеры:
        >>> my_car = Car("Audi", "A4", 2019)
        >>> descript_car = my_car.get_descriptive_name()
        """
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def get_odometer(self) -> int:
        """
        Функция возвращает пробег автомобиля в километрах

        :return: Пробег автомобиля в километрах

        Примеры:
        >>> my_car = Car("Audi", "A4", 2019)
        >>> odomometr_val = my_car.get_odometer()
        """
        return self.odometer_reading

    def increment_odometer(self, km: int = 0) -> None:
        """
        Функция увеличивает показания одометра

        :param km: Значение в километрах
        :raise TypeError: Если тип введенного значения отличается от integer,
        то возвращается ошибка.
        :raise ValueError: Если введённое значение меньше 0, то возвращается ошибка.

        Примеры:
        >>> my_car = Car("Audi", "A4", 2019)
        >>> my_car.increment_odometer(15)
        """
        if not (isinstance(km, int)):
            raise TypeError("km должен иметь тип integer")
        if km < 0:
            raise ValueError("Значение km не может быть отрицательным")
        self.odometer_reading += km


class Battery:
    """Модель аккумулятора"""
    def __init__(self, battery_size: int = 100, batt_charge_val: int = 0):
        """
        Создание и подготовка к работе объекта "Машина"

        :param battery_size: Размер аккумулятора. Значение по умолчанию 100
        :param batt_charge_val: Заряд аккумулятора. Значение по умолчанию 0

        Примеры:
        >>> my_battery = Battery(100, 50) # инициализация экземпляра класса
        """
        if not (isinstance(battery_size, int)):
            raise TypeError("battery_size имеет тип integer")
        if batt_charge_val < 0:
            raise ValueError("battery_size не может быть отрицательным")
        if not (isinstance(batt_charge_val, int)):
            raise TypeError("batt_charge_val имеет тип integer")
        if not 0 <= batt_charge_val <= battery_size:
            raise ValueError("batt_charge_val принимает значения от 0 до battery_size")
        self.battery_size = battery_size
        self.batt_charge_val = batt_charge_val

    def get_batt_charge_val(self) -> int:
        """
        Функция дает возможность получить значение заряда аккумулятора

        :return: Заряд аккумулятора

        Примеры:
        >>> my_battery = Battery(1000, 500)
        >>> my_battery.get_batt_charge_val()
        """
    def charge_battery(self, charge_val: int = 1) -> None:
        """
        Функция увеличивает заряд аккумулятора на введёенное значение

        :param charge_val: Значение на которое необходимо увеличить заряд аккумулятора.
        Значение по умолчанию 1
        :raise TypeError: Если тип введенного значения отличается от integer,
        то возвращается ошибка.
        :raise ValueError: Если введённое значение меньше 0, то возвращается ошибка.

        Примеры:
        >>> my_battery = Battery(1000, 500)
        >>> my_battery.charge_battery(100)
        """
        if not (isinstance(charge_val, int)):
            raise TypeError("charge_val имеет тип integer")
        if charge_val < 0:
            raise ValueError("charge_val не может быть отрицательным числом")
        if charge_val + self.batt_charge_val > self.battery_size:
            self.batt_charge_val = self.battery_size
        else:
            self.batt_charge_val += charge_val


if __name__ == "__main__":
    doctest.testmod()
