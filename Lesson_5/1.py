"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import namedtuple
CI = namedtuple('Company', 'name First Second Third Fourth')


def input_namedtuple():
    """Функция запрашивает данные для заполнения именного кортежа"""
    company_info = CI(name=input("Введите название компании: "),
                      First=int(input("Введите прибыль за первый квартал: ")),
                      Second=int(input("Введите прибыль за второй квартал: ")),
                      Third=int(input("Введите прибыль за третий квартал: ")),
                      Fourth=int(input("Введите прибыль за четвертый квартал: ")))
    return company_info


def average_income(info, count):
    """Функция считае среднюю прибыль по всем компаниям"""
    total_income = 0
    for company in range(count):
        total_income += (info[company].First + info[company].Second + info[company].Third +
                         info[company].Fourth)
    return total_income / count


def company_income(company):
    """Общая прибыль у отдеьно взятой фирмы"""
    return company.First + company.Second + company.Third + company.Fourth


def above_average_company(info, avg_res, count):
    """Отсортировка по двум спискам, компании с доходом выше среднего и оставшиеся(ниже среднего)"""
    best = []
    residue = []
    for i in range(count):
        if company_income(info[i]) > avg_res:
            best.append(info[i].name)
        else:
            residue.append(info[i].name)
    return best, residue


COUNT = int(input('Введите количество компаний для расчетов: '))
INFO = [(input_namedtuple()) for i in range(COUNT)]
# print(INFO)
AVG_RES = average_income(INFO, COUNT)
print(f"Средняя прибыль {AVG_RES}/год")
BESTS, REST = above_average_company(INFO, AVG_RES, COUNT)
print(f"Прибыль выше среднего у компании(й) {BESTS}"
      f"\n Прибыль ниже среднего у компании(й) {REST}")
