#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def _init_(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def _init_(self, name, surname, position, wage, bonus):
        super()._init_(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self.name + '' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

r = Position("Ivan", "Ivanov", "manager", 50000, 20000)
print(r.get_full_name())
print(r.position())
print(r.get_total_income())





