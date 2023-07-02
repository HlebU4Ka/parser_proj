class Vacancy:
    """
    Класс для сравнения заданных параметров вакансии.
    """
    def __init__(self, name: str, salary: int, exp: str,
                 address: str, city: str, url: str):
        self.__name = name
        self.__exp = exp
        self.__city = city
        self.__url = url
        self.__address = address
        if salary is None:
            self.__salary = salary
        else:
            self.__salary = 0

    @property
    def salary(self):
        return self.__salary

    """
    Сравнение вакансий дандер методами
    """

    def __gt__(self, other):
        """
         Этот метод сравнивает текущий объект с другим объектом,
         используя оператор "больше" (>). Он возвращает True,
         если текущий объект больше другого объекта, и
         False в противном случае.
        :param other:
        :return:
        """
        return self.__salary > other.__salary

    def __ge__(self, other):
        """
        Этот метод сравнивает текущий объект с другим объектом,
        используя оператор "больше или равно" (>=).
        Он возвращает True, если текущий объект больше или равен другому объекту,
        и False в противном случае.
        :param other:
        :return:
        """
        return self.__salary >= other.__salary

    def __lt__(self, other):
        """
        Этот метод сравнивает текущий объект с другим объектом,
        используя оператор "меньше" (<).
        Он возвращает True, если текущий объект меньше другого объекта,
        и False в противном случае.
        :param other:
        :return:
        """
        return self.__salary < other.__salary

    def __le__(self, other):
        """
         Этот метод сравнивает текущий объект с другим объектом,
         используя оператор "меньше или равно" (<=).
         Он возвращает True, если текущий объект меньше или равен другому объекту,
         и False в противном случае.
        :param other:
        :return:
        """
        return self.__salary <= other.__salary

    def __eq__(self, other):
        """
        Этот метод сравнивает текущий объект с другим объектом,
        используя оператор "равно" (==). Он возвращает True,
        если текущий объект равен другому объекту,
        и False в противном случае
        :param other:
        :return:
        """
        return self.__salary == other.__salary

    def __str__(self):
        """
        Этот метод возвращает строковое представление объекта.
        Он используется, когда объект преобразуется в строку с помощью функции str().
        :return:
        """
        return f"{self.__name}, {self.__salary}, {self.__exp}, " \
               f"{self.__city}, {self.__url}, {self.__address}"

    def __repr__(self):
        return f"{self.__class__.__name__}, {self.__salary}, {self.__exp}, " \
               f"{self.__city}, {self.__url}, {self.__address}"
