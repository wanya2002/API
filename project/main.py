from classes import HeadHunter, SuperJob
from selection import Selector
from vacancies import Vacancy


def main():
    vacancies_json = []
    keyword = input("Введите ключевое слово для поиска вакансий \n")

    hh = HeadHunter(keyword)
    num = input("Введите количество страниц для отображения вакансий\n")
    hh.get_vacancies(page_count=int(num))
    sb = SuperJob(keyword)
    sb.get_vacancies(page_count=int(num))
    vacancies_json.extend(hh.get_formatted_vacancies())
    vacancies_json.extend(sb.get_formatted_vacancies())
    print()

    selector = Selector(keyword, vacancies_json)
    vacancy = Vacancy(selector.vacancies())

    while True:
        res = input('Выберите действие:\n 1 - Вывести перечень всех вакансий\n 2 - '
                    'Вывести отсортированный список по зарплате\n'
                    ' 3 - Вывести список вакансий с платформы HeadHunter или SuperJob\n'
                    ' 4 - Выйти из программы\n\n ')
        if res == '1':
            vacancy.select()
        elif res == '2':
            vacancy.sort_by_salary_from()
        elif res == '3':
            api = input('Наберите платформу HeadHunter или SuperJob\n')
            if api == 'HeadHunter' or api == 'SuperJob':
                vacancy.sort_by_api(api)
            else:
                quit(print('Вы набрали несуществующую платформу'))
        elif res == '4':
            quit(print('Выход из программы'))


if __name__ == "__main__":
    main()

