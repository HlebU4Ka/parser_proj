
from abc import ABC, abstractmethod
import httpx
import ujson

SUPERJOB_API = ("https://www.superjob.ru/2.0/vacancies/")
api = "v3.r.137628441.065b9b8deae7dce637fcff2952f982e386912ba2.e9067c71aa6de6605c3d46f5446f11c25c640834"


class JobSiteAPI(ABC):

    @abstractmethod
    def get_content(self):
        pass


class HHAPI(JobSiteAPI):
    """
    Класс для получения данных с hh.ru
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.__params = {
            "text": "NAME:" + self.name,
            "page": 0,
            "per_page": 100
        }

    def get_content(self) -> dict:
        """
        Метод для получения данных по заданной вакансии
        :return: список вакансий в формате json
        """
        hh_req = httpx.get('https://api.hh.ru/vacancies', params=self.__params)
        hh_row_data = hh_req.content.decode()
        hh_json = ujson.loads(hh_row_data)

        return hh_json

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"


class SuP_job_API(JobSiteAPI):
    """
       Класс для получения данных с www.superjob.ru
    """
    #api: str = os.environ.get("SUPERJOB_API")
    headers = {
        'Host': 'api.superjob.ru',
        'X-Api-App-Id': api,
        'Authorization': 'Bearer r.000000010000001.example.access_token',
        'Content-Type': 'application / x-www-form-urlencoded',
    }

    def __init__(self, name):
        self.name = name
        self.__params = {
            'keywords': [self.name],  # Название вакансии
            'payment_from': 0,  # зарплата от
            'published': 1,

        }

    def get_content(self) -> dict:
        """
        Метод для получения данных по заданной вакансии
        :return: список вакансий в формате json
        """
        get_info = httpx.get('https://www.superjob.ru/2.0/vacancies/',
                             params=self.__params,
                             headers=self.headers
                             )
        row_date = get_info.content.decode()
        supj_json = ujson.loads(row_date)

        return supj_json

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"

# hh_api = HHAPI("Python")
# hh_jobs = hh_api.get_content()
# print(hh_jobs)
#
# sup_api = SuP_job_API("Python")
# sup_jobs = sup_api.get_content()
# print(sup_jobs)