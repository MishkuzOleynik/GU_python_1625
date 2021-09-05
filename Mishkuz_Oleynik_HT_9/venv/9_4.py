# не нужно в потомках переопределять инициализаццию
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула на{direction}')

    def show_speed(self):
        print(f'Скорость движения машины: {self.speed}')

    def check_police(self):
        print(self.is_police)


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= 60 else print('Превышении скорости 60' )


class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= 40 else print('Превышении скорости 40' )

class PoliceCar(Car):
    is_police = True


car = Car(45, 'grey', 'BMW')
town_car = TownCar(70, 'green', 'Opel')
sport_car = SportCar(80, 'black', 'Ferrari')
work_car = WorkCar(30, 'yellow', 'BobCat')
police_car = PoliceCar(50, 'white', 'Ford', True)

town_car.go()
town_car.turn('право')
town_car.show_speed()
town_car.stop()
car.check_police()
print(f'\n \n Модель: {town_car.name} \n Color: {town_car.color} \n Speed: {town_car.speed} \n '
      f'Is Police car: {town_car.is_police}' )

police_car.check_police()



