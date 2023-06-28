import ujson

from src.saver import Json_Save, TXT_Save
from src.vacancy import Vacancy
from src.get_content import HHAPI, SuP_job_API

def user_interact():

    search_vacancy = input("Введите название профессии: ")
    hh = HHAPI(search_vacancy)
    get_hh = hh.get_content()

    sup_ojb = SuP_job_API(search_vacancy)
    get_sup_ojb = sup_ojb.get_content()

    saver_json = Json_Save()
    saver_TXT = TXT_Save()

    for i in get_hh["items"]:
        address = i["address"]
        salary = i["salary"]

        if i["salary"] is not None:
            salary = i['salary']['street']

        type_experience = {'Нет опыта': 'Без опыта',
                       'От 1 года до 3 лет': "От 1 года",
                        'От 3 до 6 лет': 'От 3 лет',
                       'Более 6 лет': 'От 6 лет',
                       'Не имеет значения': 'Без опыта'}

        exp = type_experience[i["experience"], ["name"]]

        vacancy = Vacancy(i['name'], salary, exp,
                      address, i['employment']['name'], i['area']['name'],
                      i['alternate_url'], i['snippet']['requirement'])

        saver_json.job_adding(vacancy.__dict__)
        saver_TXT.job_adding(vacancy.__dict__)

    for i in get_sup_ojb["objects"]:
        vacancy = Vacancy(i['profession'], i['payment_from'], i['experience']['title'],
                          i['address'], i['type_of_work']['title'],
                          i['town']['title'], i['link'], i['candidat'])

        saver_json.job_adding(vacancy.__dict__)
        saver_TXT.job_adding(vacancy.__dict__)

    try:
        params_city = saver_json.get_city(input("Укажите город для поиска: "))
        param_salary = saver_json.get_salary(int(input("Укажите зарплату для поиска: ")))
        params_exp = saver_json.get_experience(input("""Укажите опыт работы для поиска("Без опыта", "От 1 года",\
"От 3 лет"): """))
        vacancy_number = int(input('Укажите количества вакансий для вывода: '))

    except TypeError as e:
        print(f'{e}("Количество вакансий и зарплата должны быть числами")')


