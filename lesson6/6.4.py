#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f' {self.name} едет со скоростью {self.speed}')

        if self.speed > 40:
            return f' {self.name} превышает скоростной режим'
        else:
            return f' {self.name} не привышает скоростной режим'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')

        if self.speed > 60:
            return f'{self.name} превышает скоростной режим'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} не полицейская машина'


bmw = SportCar(100, 'Red', 'BMW', False)
lada = TownCar(30, 'White', 'Lada', False)
kamaz = WorkCar(70, 'Rose', 'Kamaz', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(kamaz.turn_left())
print(f'When {lada.turn_right()}, then {bmw.stop()}')
print(f'{kamaz.go()} with speed exactly {kamaz.show_speed()}')
print(f'{kamaz.name} is {kamaz.color}')
print(f'Is {bmw.name} a police car? {bmw.is_police}')
print(f'Is {kamaz.name}  a police car? {kamaz.is_police}')
print(bmw.show_speed())
print(lada.show_speed())
print(ford.police())
print(ford.show_speed())




