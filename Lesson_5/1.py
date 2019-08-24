# -*- coding: utf-8 -*-
"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple, OrderedDict


def input_companies():
    companies = []
    company_description = namedtuple("CompanyProfit", "name Q1 Q2 Q3 Q4", defaults=[0])
    company_number = int(input("Введите количество компаний: "))
    for i in range(company_number):
        name = input("Введите имя компании: ")
        profit = (float(i)
                  for i in input("Введите прибыль компании по кварталам через запятую,"
                                 "например, 120,101.5,33,58: ").split(','))
        company = company_description(name, *profit)
        companies.append(company)

    return companies


def calculate_early(companies):
    values = OrderedDict()
    for company in companies:
        values.update({company.name: company.Q1 + company.Q2 + company.Q3 + company.Q4})
    return values


def get_average_early_profit(early_profit_per_company):
    return sum(early_profit_per_company.values()) / len(early_profit_per_company)


def get_above_and_below_average_profit(company_early_profit, average_profit):
    above, below = [], []
    for company, profit in early_profit_per_company.items():
        if profit < average_profit:
            below.append(company)
            continue
        if profit > average_profit:
            above.append(company)
    return above, below


if __name__ == "__main__":
    companies = input_companies()

    early_profit_per_company = calculate_early(companies)
    average_profit = get_average_early_profit(early_profit_per_company)
    print(f"Средняя прибыль за год для всех предприятий: {average_profit}")

    above_average, below_average = get_above_and_below_average_profit(early_profit_per_company, average_profit)
    print(f"Компании, у которых прибыль выше среднего: {', '.join(above_average)}")
    print(f"Компании, у которых прибыль ниже среднего: {', '.join(below_average)}")
