

class Vacancy:
    """Создаем класс Vacancy для работы с вакансиями"""


    def __init__(self, vacancies):
        self.vacancies = vacancies


    def select(self):
        """Выводим список вакансий"""
        for vacancy in self.vacancies:
            print(f'\nРаботодатель: {vacancy["employer"]}\nНаименование вакансии: {vacancy["title"]}\n'
                  f'Ссылка: {vacancy["url"]}\n'
                  f'Платформа: {vacancy["api"]}\nЗарплата от: {vacancy["salary_from"]}\n'
                  f'Зарплата до: {vacancy["salary_to"]}\nВалюта: {vacancy["currency"]}')


    def sort_by_salary_from(self):
        """Выводим отсортированный список вакансий по зарплате"""
        self.vacancies = sorted(self.vacancies, key=lambda i: (i['salary_from'] if i['salary_from'] else 0), reverse=False)
        for vacancy in self.vacancies:
            print(f'\nРаботодатель: {vacancy["employer"]}\nНаименование вакансии: {vacancy["title"]}\n'
                  f'Ссылка: {vacancy["url"]}\n'
                  f'Платформа: {vacancy["api"]}\nЗарплата от: {vacancy["salary_from"]}\n'
                  f'Зарплата до: {vacancy["salary_to"]}\nВалюта: {vacancy["currency"]}')


    def sort_by_api(self, api):
        """Выводим отсортированный список по названию платформы"""
        self.api = api
        for vacancy in self.vacancies:
            if vacancy["api"] == self.api:
                print(f'\nРаботодатель: {vacancy["employer"]}\nНаименование вакансии: {vacancy["title"]}\n'
                      f'Ссылка: {vacancy["url"]}\n'
                      f'Платформа: {vacancy["api"]}\nЗарплата от: {vacancy["salary_from"]}\n'
                      f'Зарплата до: {vacancy["salary_to"]}\nВалюта: {vacancy["currency"]}')