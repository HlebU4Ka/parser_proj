import os
from abc import ABC, abstractmethod
import httpx
import ujson

SUPERJOB_API = ("https://2647.superjob.ru/2.0/vacancies")


class JobSiteAPI(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_jobs(self):
        pass


class HHAPI(JobSiteAPI):

    def __init__(self, name: str) -> None:
        self.__params = None
        self.name = name

    def connect(self):
        """
        Метод для получения данных по заданной вакансии
        :return: список вакансий в формате json
        """
        hh_req = httpx.get('https://api.hh.ru/vacancies', params=self.__params)
        hh_row_data = hh_req.content.decode()
        hh_json = ujson.load(hh_row_data)

        return hh_json

    def get_jobs(self) -> dict:
        """
        Метод для получения данных по заданной вакансии
        """
        self.__params = {
            "text": "NAME:" + self.name,
            "page": 0,
            "per_page": 100
        }

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"


class SuP_job_API(JobSiteAPI):
    api: str = os.environ.get("SUPERJOB_API")
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



    def get_jobs(self):
        """
        Метод для получения данных по заданной вакансии
        :return: список вакансий в формате json
        """
        get_info = httpx.get('SUPERJOB_API',
                             params=self.__params,
                             headers=self.headers
                             )
        row_date = get_info.content.decode()
        supj_json = ujson.load(row_date)

        return supj_json

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"
