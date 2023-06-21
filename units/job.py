class Job:
    """
    Класс, представляющий информацию о вакансии.

    Attributes:
        title (str): Название вакансии.
        link (str): Ссылка на вакансию.
        salary (float): Зарплата.
        description (str): Краткое описание или требования.

    Methods:
        __repr__: Возвращает строковое представление объекта.
        __eq__: Проверяет равенство двух вакансий по зарплате.
        __lt__: Проверяет, является ли зарплата текущей вакансии меньше, чем у другой.
        __gt__: Проверяет, является ли зарплата текущей вакансии больше, чем у другой.
        Validate_data: Проверяет корректность данных, инициализирующих атрибуты вакансии.
    """

    def __init__(self, title, link, salary, description):
        """
        Инициализирует объект Job.

        Args:
            title (str): Название вакансии.
            link (str): Ссылка на вакансию.
            salary (float): Зарплата.
            description (str): Краткое описание или требования.
        """
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __repr__(self):
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Job(title='{self.title}', salary='{self.salary}')"

    def __eq__(self, other):
        """
        Проверяет равенство двух вакансий по зарплате.

        Args:
            other (Job): Другой объект Job для сравнения.

        Returns:
            bool: True, если зарплаты равны. Иначе False.
        """
        return self.salary == other.salary

    def __lt__(self, other):
        """
        Проверяет, является ли зарплата текущей вакансии меньше, чем у другой.

        Args:
            other (Job): Другой объект Job для сравнения.

        Returns:
            bool: True, если зарплата текущей вакансии меньше. Иначе False.
        """
        return self.salary < other.salary

    def __gt__(self, other):
        """
        Проверяет, является ли зарплата текущей вакансии больше, чем у другой.

        Args:
            other (Job): Другой объект Job для сравнения.

        Returns:
            bool: True, если зарплата текущей вакансии больше. Иначе False.
        """
        return self.salary > other.salary

    def validate_data(self):
        """
        Проверяет корректность данных, инициализирующих атрибуты вакансии.
        Raises:
                    ValueError: Если данные некорректны.
                """
        if not isinstance(self.title, str):
            raise ValueError("Job title must be a string.")

        if not isinstance(self.link, str):
            raise ValueError("Job link must be a string.")

        if not isinstance(self.salary, (int, float)):
            raise ValueError("Job salary must be a number.")

        if not isinstance(self.description, str):
            raise ValueError("Job description must be a string.")