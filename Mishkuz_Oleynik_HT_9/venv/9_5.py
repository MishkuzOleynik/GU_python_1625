class Stationary:
    title = 'Parent'

    def draw(self):
        print(f'Запуск рисования {self.title}')

class Pen(Stationary):
    title = 'Pen'

    def draw(self):
        print(f'Запуск рисования {self.title}')

class Pencil(Stationary):
    title = 'Pencil'

    def draw(self):
        print(f'Запуск рисования {self.title}')

class Hndle(Stationary):
    title = 'Handle'

    def draw(self):
        print(f'Запуск рисования {self.title}')


parent = Stationary()
pen = Pen()
pencil = Pencil()
handle = Hndle()

parent.draw()
pen.draw()
pencil.draw()
handle.draw()
