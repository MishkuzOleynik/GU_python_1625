class Road:
    def __init__(self, lenght, width):
        self._length = int(lenght)
        self._width = int(width)

    def count_weight(self, layer):
        weight = (layer * self._length * self._width * 25) / 1000
        print(f' Масса асфальта: {weight} тонн')

lenght = input('Введите значение длины дорожного покрытияб м: ')
width = input('Введите значение ширины дорожного покрытия, м: ')
layer = int(input('Введите значение толщины слоя дорожного покрытияб см: '))
my_road = Road(lenght,width)
my_road.count_weight(layer)
