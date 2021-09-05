# class Auto:
#     auto_count = 0
#
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print('Автомобиль заведен')
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1
#
# a = Auto()
# a.on_auto_start()



class Auto:
    auto_count = 0


    def  __init__(self):
        print("Автомобиль заведен")
        self.auto_name = "Mazda"
        self._auto_year = "1998"
        self._auto_model = "CX9"
        Auto.auto_count += 1

a = Auto()
b = Auto()
print(a.auto_name)
print(a._auto_year)
print(a._auto_model)
print(a.auto_count)




