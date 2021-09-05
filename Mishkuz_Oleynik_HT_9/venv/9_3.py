class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage' : wage, 'bonus' : bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'Фамилия имя сотрудника: {self.surname} {self.name}')

    def get_total_income(self):
        print(f'Общий доход: {sum(self._income.values())} {self._income}')

worker = Position('Кондрат', 'Митяев', 'Дворник', 30000 ,10000)
worker.get_full_name()
worker.get_total_income()