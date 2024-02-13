class Car:
    def __init__(self, power: int, max_passengers: int):
        """
        :param power: мощность двигателя
        :param max_passengers: максимальное количестов пассажиров
        """
        if not isinstance(power, (int, float)):
            raise TypeError("Мощность должна быть int или float")
        if power <= 0:
            raise ValueError("Мощность должна быть положительным числом")
        self.power = power
        if not isinstance(max_passengers, (int)):
            raise TypeError("максимальное количестов пассажиров int ")
        if max_passengers <= 0:
            raise ValueError("максимальное количестов пассажиров должно быть положительным числом")
        self.max_passengers = max_passengers
    def add_power(self, plus_power: int) -> None:
        """

        :param plus_power: добавляемая мощность
        :return: мощность двигателя после модернизации

        >>> car = Car(200,4)
        >>> car.add_power(50)
        """
    def capacity(self) -> None:
        """
        Проверка поместяться ли пассажиры в машину
        :return: Поместяться или нет
         >>> car = Car(150,3)
         >>> car.capacity()
        """
class Weapon:
    def __init__(self, ammo_in_clip: int, clip_capacity: int):
        """
        :param ammo_in_clip: патронов в обойме
        :param clip_capacity: вместимость обоймы
        """
        if not isinstance(ammo_in_clip, int):
            raise TypeError("Патроны должны быть int ")
        if ammo_in_clip <= 0:
            raise ValueError("Патроны должны быть положительным числом")
        self.ammo_in_clip = ammo_in_clip
        if not isinstance(clip_capacity, int):
            raise TypeError("Патронов в обойме int ")
        if clip_capacity <= 0:
            raise ValueError("Патронов в обойме должно быть положительным числом")
        self.clip_capacity = clip_capacity
    def is_empty(self)-> bool:
        """
        Проверка пустой ли магазин
        :return: Пустой или нет
        >>> ak47 = Weapon(20,30)
        >>> ak47.is_empty()
        """
    def add_ammo(self, plus_ammo)-> int:
        """

        :param plus_ammo: Количестов добавляемых патрон
        :return: Магазин с добавленными патронами
        >>> ak47 = Weapon(10,30)
        >>> ak47.add_ammo(5)
        """
        if not isinstance(plus_ammo, int):
            raise TypeError("Патроны должны быть int ")
class Monitor:
    def __init__(self,resolution: list, cost: (int, float), matrix: str):
        """

        :param resolution: Разрешение монитора
        :param cost: Стоимость монитра
        :param matrix: Матрица в мониторе
        """
        if not isinstance(resolution, list):
            raise TypeError("Разрешение должно быть list ")
        if not isinstance(cost, (int, float)):
            raise TypeError("Цена должна быть int или float ")
        if cost <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.cost = cost
        if not isinstance(matrix, str):
            raise TypeError("Матрица должна быть str ")
    def resolution_check(self)->bool:
        """

        :return: Может ди быть такое разрешение
        >>> monitor = Monitor([1920, 1080],15000,"ips")
        >>> monitor.resolution_check()
        """
    def sale(self, discount: int):
        """

        :param discount: Скидка на монитор
        :return: Цена со скидкой
        >>> monitor = Monitor([1920, 1080],15000,"ips")
        >>> monitor.sale(500)
        """
    def color(self)->bool:
        """

        :return: Хорошая ли цветопреедача
        >>> monitor = Monitor([1920, 1080],15000,"ips")
        >>> monitor.color()
        """
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
