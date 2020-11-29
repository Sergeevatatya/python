#2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def take_cloth3(self):
        return str(f'Площадь общая ткани \n'
               f'{round(self.width / 6.5 + 0.5) + round(self.height * 2 + 0.3)}')

class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.take_cloth = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Ткани на пальто понадобится: {self.take_cloth}'

class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.take_clothes2 = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Ткани на костюм понадобится: {self.take_clothes2}'

clothes = Clothes(2, 5)
coat = Coat(2, 8)
suit = Suit(4, 5)
print(coat)
print(suit)
print(clothes.take_cloth3)











