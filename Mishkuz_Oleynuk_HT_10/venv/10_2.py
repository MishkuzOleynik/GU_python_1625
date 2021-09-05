from abc import abstractclassmethod, ABC




class Clothes(ABC):
    @abstractclassmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suite(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return self.h/100 * 2 + 0.3


coat_1 = Coat(52)
coat_2 = Coat(46)

suite_1 = Suite(167)
suite_2 = Suite(192)

print(coat_1.consumption)
print(coat_2.consumption)
print(suite_1.consumption)
print(suite_2.consumption)

