

def main():
    # Создание экземпляров классов для работы с API сайтов с вакансиями
    hh_api = pass
    supejob_api = pass

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies("Python")
    superjob_vacancies = supejob_api.get_vacancies("Python")

    # Запрос информации у пользователя
    platform = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите поисковый запрос: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

def get_user_platform():
    platform = input("Введите платформу (HeadHunter или SuperJob): ")
    return platform

user_platform = get_user_platform()