# Класс автобус обыкновенный
class Bus:
    def __init__(self, FIO, Number, Route, Model, Year, Mileage):
        self.FIO = FIO
        self.Number = Number
        self.Route = Route
        self.Model = Model
        self.Year = Year
        self.Mileage = Mileage

    def __str__(self):
        return "Водитель: " + str(self.FIO) + ", Госномер: " + str(self.Number) + ", Маршрут: " + str(self.Route) + ", Марка: " + str(self.Model) + ", Год выпска: " + str(self.Year) + ", Пробег: " + str(self.Mileage)

    def ReturnRoutes (self, Routes):
        if self.Route == Routes:
            return self.Route

    def ReturnAges (self, Mileages):
        if self.Mileage > Mileages:
            return self.Mileage

# Список автобусов с данными
Buses = [
    Bus("Пупкин В.С", "ВО 1234-7", 1, "Ikarus", 1980, 10000),
    Bus("Ложкин В.С", "ВО 1234-6", 1, "Mercedes", 1985, 20000),
    Bus("Вилкин В.С", "ВО 1234-5", 1, "Scania", 1990, 30000),
    Bus("Тарелкин В.С", "ВО 1234-4", 2, "Fiat", 1995, 40000),
    Bus("Кастрюлькин В.С", "ВО 1234-3", 2, "MAN", 2000, 50000),
    Bus("Сковородкин В.С", "ВО 1234-2", 2, "MAZ", 2005, 60000)
]

# Выводим список автобусов для заданного номера маршрута
Routes = 1

for b in Buses:
    if b.ReturnRoutes(2) is not None:
        print ("По маршруту номер " + str(Routes) + " ходят следующие автобусы: " + str(b))

# Выводим список автобусов, которые эксплуатируются больше заданного срока;
Mileage = 30000

print ("\n")
for b in Buses:
    if b.ReturnAges(5) > Mileage:
        print ("С пробегом более " + str(Mileage) + " ходят следующие автобусы: " + str(b))