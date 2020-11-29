#3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
#Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
#Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
#Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
#В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
#Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
# аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**.
#Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
#Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, num):
        self.num = int(num)
    def __str__(self):
        return f'Количество клеток: {self.num}'
    def __add__(self, other):
        self.result = Cell(self.num + other.num)
        return f'Сумма клеток равна: {self.result}'
    def __sub__(self, other):
        if self.num >= other.num:
            self.result1 = Cell(int(self.num - other.num))
            return self.result1
        else:
            return
    def __mul__(self, other):
        self.result2 = Cell(self.num * other.num)
        return f'Результат деления клеток: {self.result2}'
    def __truediv__(self, other):
        self.result3 = Cell(round(self.num / other.num))

    def make_order(self, cell_row):
        a = ''
        for i in range(int(self.num / cell_row)):
            a += f'{"*" * cell_row} \\n'
        a += f'{"*" * (self.num % cell_row)}'
        return a

cell1 = Cell(25)
other = Cell(5)
print(cell1)
print(cell1 + other)
print(cell1 - other)
print(other.make_order(5))
print(cell1.make_order(10))
print(cell1 * other)
print(cell1 / other)



