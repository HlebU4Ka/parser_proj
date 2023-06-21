import requests
import json
from bs4 import BeautifulSoup

# Отправка GET-запроса к странице Python на сайте
url = "https://api.hh.ru/vacancies"
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Создание объекта BeautifulSoup для парсинга HTML-кода
    soup = BeautifulSoup(response.content, "html.parser")

    # Нахождение нужной информации на странице
    # Здесь приведен пример нахождения словаря с классом "my-dictionary"
    dictionary_element = soup.find("div", class_="my-dictionary")

    # Проверка, найден ли элемент на странице
    if dictionary_element is not None:
        # Создание пустого словаря
        dictionary = {}

        # Извлечение данных из HTML-элемента и добавление их в словарь
        for item in dictionary_element.find_all("li"):
            key = item.find("span", class_="key").text
            value = item.find("span", class_="value").text
            dictionary[key] = value

        # Сохранение словаря в JSON-файл
        with open("dictionary.json", "w") as file:
            json.dump(dictionary, file)

        print("Словарь успешно сохранен в файл dictionary.json")

    else:
        print("Элемент не найден на странице.")

else:
    print("Ошибка при получении страницы:", response.status_code)