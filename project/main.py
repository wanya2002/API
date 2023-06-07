from classes import HeadHunter, SuperJob, Selector

def main():
    vacancies_json = []
    keyword = input("Введите ключевое слово для поиска вакансий \n")

    hh = HeadHunter(keyword)
    hh.get_vacancies(page_count=2)
    sb = SuperJob(keyword)
    sb.get_vacancies(page_count=2)
    vacancies_json.extend(hh.get_formatted_vacancies())
    vacancies_json.extend(sb.get_formatted_vacancies())
    print()

    selector = Selector(keyword, vacancies_json)

    while True:
        res = input('Выберите действие:\n 1 - Вывести перечень всех вакансий\n 2 - '
                    'Вывести отсортированный список по зарплате\n'
                    ' 3 - Вывести список вакансий с платформы HeadHunter или SuperJob\n'
                    ' 4 - Выйти из программы\n\n ')
        if res == '1':
            selector.vacancies()
        elif res == '2':
            selector.sort_by_salary_from()
        elif res == '3':
            api = input('Наберите платформу HeadHunter или SuperJob\n')
            if api == 'HeadHunter' or api == 'SuperJob':
                selector.sort_by_api(api)
            else:
                quit(print('Вы набрали несуществующую платформу'))
        elif res == '4':
            quit(print('Выход из программы'))

if __name__ == "__main__":
    main()

