#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        day_today = []
        for i in day_month_year.split():
            if i != '-': day_today.append(i)
        return int(day_today[0]), int(day_today[1]), int(day_today[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Дата введена верно'
                else:
                    return f'Неправильно введен год'
            else:
                return f'Неправильно введен месяц'
        else:
            return f'Неправильно введен день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('27 - 11 - 2020')
print(today)
print(Data.valid(23, 7, 2024))
print(today.valid(31, 50, 1900))
print(Data.extract('27 - 11 - 2020'))
print(today.extract('27 - 11 - 2021'))
print(Data.valid(25, 10, 2000))



