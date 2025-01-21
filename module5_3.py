# Домашняя работа по уроку "Перегрузка операторов"

class House:
# создаем метод инициализации/конструкт
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
# создаем методы
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self

    def __radd__(self, other):
        if isinstance(other, int):
            return House(self.name, other + self.number_of_floors)

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


# создаем объект/экземпляр класса
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# str
print(h1)
print(h2)

# __eq__
print(h1 == h2)

# __add__
h1 = h1 + 10
print(h1)
print(h1 == h2)

# __iadd__
h1 += 10
print(h1)

# __radd__
h2 = 10 + h2
print(h2)
#===============================================================
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
#===============================================================

# RESULT:
"""""
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False
"""""