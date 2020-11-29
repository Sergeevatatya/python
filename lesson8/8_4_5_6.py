#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#5.Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.
#6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.




class OrgTechnic:
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.orgtech = {'Модель': self.name, 'Цена': self.price, 'Количество': self.quantity}
        self.list_store = []
        self.full_list_store = []
    def __str__(self):
        return f'Цена: {self.price} Количесто: {self.quantity}'

    def reception(self):
        try:
            name1 = input(f'Введите наименование ')
            price1 = int(input(f'Введите цену за ед '))
            quantity1 = int(input(f'Введите количество '))
            common = {'Модель': name1, 'Цена': price1, 'Количество': quantity1}
            self.orgtech.update(common)
            self.list_store.append(self.orgtech)
            print(f'Текущий список -\n {self.list_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - M, продолжение - Enter')
        m = input('M/ Enter')
        if m == 'M' or m == 'm':
            self.full_list_store.append(self.list_store)
            print(f'Весь склад -\n {self.full_list_store}')
            return f'Выход'
        else:
            return OrgTechnic.reception(self)

class Printer(OrgTechnic):
        def count(self):
            return f'{self.orgtech}'

class Scanner(OrgTechnic):
        def count(self):
            return f'{self.orgtech}'

class Copier(OrgTechnic):
        def count(self):
            return f'{self.orgtech}'

unit_1 = Printer('hp', 2020, 10, 101)
unit_2 = Scanner('Canon', 1200, 4, 101)
unit_3 = Copier('Xerox', 1558, 25, 25)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.count())
print(unit_2.count())
print(unit_3.count())




