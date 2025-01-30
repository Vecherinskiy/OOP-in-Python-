"""Лабораторная работа 4"""

import doctest


class Car:
    """Простая модель автомобиля"""
    def __init__(self, car_brand: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param car_brand: Марка машины
        :param model: Модель
        :param year: Год выпуска

        Примеры:
        >>> my_car = Car("Audi", "A4", 2019) # инициализация экземпляра класса
        """
        self._car_brand = car_brand
        self._model = model
        self._year = year
        self._odometer_reading = 0  # пробег машины
        self._num_fuel = 0  # количество топлива
        self._fuel_tank_size = 1000  # размер топливного бака

    @property
    def car_brand(self) -> str:
        """
        Функция позволяет получить значение марки автомобиля

        :return: Марка автомобиля

        Пример:
        >>> my_car = Car("Audi", "A4", 2019)
        >>> my_car_brand = my_car.car_brand
        """
        return self._car_brand

    @car_brand.setter
    def car_brand(self, car_brand: str = None) -> None:
        """
        Функция изменяет значение self._car_brand

        :param car_brand: Марка автомобиля
        :raise TypeError: Если тип введенного значения отличается от str,
        то возвращается ошибка.

        Пример:
        >>> my_car = Car
        >>> my_car.car_brand = "Audi"
        """
        if not isinstance(car_brand, str):
            raise TypeError("car_brand must be str")
        self._car_brand = car_brand

    @property
    def model(self) -> str:
        """
        Функцияпозволяет получить значение модели автомобиля

        :return: Модель автомобиля

        Пример:
        >>> my_car = Car("Audi", "A4", 2019)
        >>> my_car_model = my_car.model
        """
        return self._model

    @model.setter
    def model(self, model: str = None) -> None:
        """
        Функция изменяет значение self._model

        :param model: Модель автомобиля
        :raise TypeError: Если тип введенного значения отличается от str,
        то возвращается ошибка.

        Пример:
        >>> my_car = Car
        >>> my_car.model = "A4"
        """
        if not isinstance(model, str):
            raise TypeError("model must be str")
        self._model = model

    @property
    def year(self) -> int:
        """
        Функция позволяет получить значение года выпуска автомобиля

        :return: Год выпуска автомобиля

        Пример:
        >>> my_car = Car("Audi", "A4", 2019)
        >>> my_car_year = my_car.year
        """
        return self._year

    @year.setter
    def year(self, year: int = None) -> None:
        """
        Функция изменяет значение self._year

        :param year: Год выпуска
        :raise TypeError: Если тип введенного значения отличается от int,
        то возвращается ошибка.
        :raise ValueError: Если введённое значение меньше 0, то возвращается ошибка.

        Пример:
        >>> my_car = Car
        >>> my_car.year = "2000"
        """
        if not isinstance(year, int):
            raise TypeError("year must be int")
        if year < 1886:
            raise ValueError("The first car did not appear until 1886 year")
        self._year = year

    @property
    def odometer_reading(self) -> int:
        """
        Функция позволяет получить показания одометра автомобиля

        :return: Показания одометра

        Пример:
        >>> my_car = Car("Audi", "A4", 2019)
        >>> odometer_val = my_car.odometer_reading
        """
        return self._odometer_reading

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
            raise TypeError("km must be int")
        if km < 0:
            raise ValueError("The km value cannot be negative")
        self._odometer_reading += km

    def fill_car(self, add_val: int = 0) -> None:
        """
        Функция увеличивает количество топлива

        :param add_val: Добавляемое значение
        :raise TypeError: Если тип введенного значения отличается от int,
        то возвращается ошибка.
        :raise ValueError: Если введённое значение меньше 0, то возвращается ошибка.

        Пример:
        >>> my_car = Car("Audi", "A4", 2019)
        >>> my_car.fill_car(100)
        """
        if not isinstance(add_val, int):
            raise TypeError("add_val must be int")
        if add_val < 0:
            raise ValueError("The add_val value cannot be negative")
        if add_val + self._num_fuel > self._fuel_tank_size:
            self._num_fuel = self._fuel_tank_size
        else:
            self._num_fuel += add_val

    def __str__(self) -> str:
        """
        Функция возврщает строковое представление класса

        :return: Строковое представление класса

        Пример:
        >>> my_car = Car("Audi", "A4", 2019)
        >>> my_car_str = str(my_car)
        """
        return (f"Автомобиль {self._car_brand} {self._model} "
                f"{self._year} года выпуска")

    def __repr__(self):
        """
        Функция возврщает строку, показывающую,
        как может быть инициализирован класс

        :return: Валидный код python

        Пример:
        >>> my_car = Car("Audi", "A4", 2019)
        >>> my_car_repr = repr(my_car)
        """
        return (f"{self.__class__.__name__}"
                f"(car_brand={self._car_brand!r}, "
                f"model={self._model!r}, "
                f"year={self._year})")


class ElectricCar(Car):
    def __init__(self, car_brand: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param car_brand: Марка машины
        :param model: Модель
        :param year: Год выпуска

        Примеры:
        >>> my_el_car = ElectricCar("Tesla", "Model S", 2020) # инициализация экземпляра класса
        """
        super().__init__(car_brand, model, year)
        self.battery_charge = 0  # заряд аккумулятора
        self.battery_size = 1000  # размер аккумулятора

    def __str__(self) -> str:
        """
        Функция возврщает строковое представление класса

        :return: Строковое представление класса

        Пример:
        >>> my_el_car = ElectricCar("Tesla", "Model S", 2020)
        >>> my_el_car_str = str(my_el_car)
        """
        return (f"Електромобиль {self._car_brand} {self._model} "
                f"{self._year} года выпуска")

    def fill_car(self, add_val: int = 0) -> None:
        """
        Функция увеличивает заряд аккумулятора
        Прегрузка нужна так как в електоромобиле вместо топливного бака акккумулятор

        :param add_val: Добавляемое значение
        :raise TypeError: Если тип введенного значения отличается от int,
        то возвращается ошибка.
        :raise ValueError: Если введённое значение меньше 0, то возвращается ошибка.

        Пример:
        >>> my_el_car = ElectricCar("Tesla", "Model S", 2020)
        >>> my_el_car.fill_car(100)
        """
        if not isinstance(add_val, int):
            raise TypeError("add_val must be int")
        if add_val < 0:
            raise ValueError("The add_val value cannot be negative")
        if add_val + self.battery_charge > self.battery_size:
            self.battery_charge = self.battery_size
        else:
            self.battery_charge += add_val


if __name__ == "__main__":
    doctest.testmod()
