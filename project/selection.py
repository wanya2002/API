import json


class Selector:
    """Создаем класс для работы с полученным списком вакансий"""


    def __init__(self, keyword, vacancies_json):
        """Инициализируем экземпляр класса"""
        self.filename = f'{keyword.title()}.json'
        self.insert(vacancies_json)


    def insert(self, vacancies_json):
        """Создаем файл-json для работы с вакансиями"""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(vacancies_json, file, indent=4)


    def vacancies(self):
        """Выводим список вакансий"""
        with open(self.filename, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
            return vacancies