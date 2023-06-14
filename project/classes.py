from abc import ABC, abstractmethod
import requests
from exception import ParsingError


class Abstr(ABC):
     """Создаем абстрактный класс с двумя методами"""
     def __init__(self):
         pass

     def __str__(self):
         return "Создаем абстрактный класс с двумя методами"

     @abstractmethod
     def get_requests(self):
         pass

     @abstractmethod
     def get_vacancies(self):
         pass


class HeadHunter(Abstr):
    """Создаем класс для парсинга с HeadHunter """

    url = 'https://api.hh.ru/vacancies'


    def __init__(self, keyword):
        """Инициализируем объект класса"""

        self.params = {
            "per_page": 100,
            "page": None,
            "text": keyword,
        }
        self.headers = {}
        self.vacancies = []


    def __str__(self):
        return "Создаем объект класса HeadHunter для получения данных о вакансиях с hh.ru"


    def get_requests(self):
        """Получаем данные"""

        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f'Ошибка получения вакансий! Статус {response.status_code}')
        return response.json()["items"]


    def get_formatted_vacancies(self):
        """Получаем список словарей с выбранными полями"""

        formatted_vacancies = []

        for vacancy in self.vacancies:
            formatted_vacancy = {
                "employer": vacancy['employer']['name'],
                "title": vacancy["name"],
                "url": vacancy["alternate_url"],
                "api": "HeadHunter",
            }

            salary = vacancy["salary"]
            if salary:
               formatted_vacancy["salary_from"] = salary['from']
               formatted_vacancy["salary_to"] = salary["to"]
               formatted_vacancy["currency"] = salary["currency"]
            else:
                formatted_vacancy["salary_from"] = None
                formatted_vacancy["salary_to"] = None
                formatted_vacancy["currency"] = None
            formatted_vacancies.append(formatted_vacancy)

        return formatted_vacancies


    def get_vacancies(self, page_count):
        """Получаем список вакансий с HeadHunter"""

        self.vacancies = []
        for page in range(page_count):
            page_vacancies = []
            self.params["page"] = page
            print(f'({self.__class__.__name__}) Парсинг страницы {page + 1}')
            try:
                page_vacancies = self.get_requests()
            except ParsingError as error:
                print(error)
            else:
                self.vacancies.extend(page_vacancies)
                print(f'Загружено вакансий: {len(page_vacancies)}')
            if len(page_vacancies) == 0:
                break


class SuperJob(Abstr):
    """Создаем класс для парсинга с SuperJob"""

    url = 'https://api.superjob.ru/2.0/vacancies/'


    def __init__(self, keyword):
        self.params = {
            "count": 100,
            "page": None,
            "keyword": keyword,
        }
        self.headers = {
            "X-Api-App-Id":"v3.r.15135658.1d7b78cff75ff4b020f758bbbfc00474f65f8645.2ebeec80f2e3874f04af1ce05f9547835d5ad7b6"
        }
        self.vacancies = []


    def __str__(self):
        return "Создаем объект класса SuperJob для получения данных о вакансиях с superjob.ru"


    def get_requests(self):
        """Функция получения данных"""

        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f'Ошибка получения вакансий! Статус {response.status_code}')
        return response.json()["objects"]


    def get_formatted_vacancies(self):
        """Получаем список словарей с выбранными полями"""

        formatted_vacancies = []

        for vacancy in self.vacancies:
            formatted_vacancy = {
                "employer": vacancy['firm_name'],
                "title": vacancy["profession"],
                "url": vacancy["link"],
                "api": "SuperJob",
                "salary_from": vacancy['payment_from'] if vacancy['payment_from'] and vacancy['payment_from'] !=0 else None,
                "salary_to": vacancy['payment_to'] if vacancy['payment_to'] and vacancy['payment_to'] !=0 else None,
                "currency": vacancy['currency'] if vacancy['currency'] else None
            }

            formatted_vacancies.append(formatted_vacancy)

        return formatted_vacancies


    def get_vacancies(self, page_count):
        """Функция получения списка вакансий"""

        self.vacancies = []
        for page in range(page_count):
            page_vacancies = []
            self.params["page"] = page
            print(f'({self.__class__.__name__}) Парсинг страницы {page + 1}')
            try:
                page_vacancies = self.get_requests()
            except ParsingError as error:
                print(error)
            else:
                self.vacancies.extend(page_vacancies)
                print(f'Загружено вакансий: {len(page_vacancies)}')
            if len(page_vacancies) == 0:
                break




























































