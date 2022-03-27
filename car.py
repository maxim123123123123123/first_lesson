class Car:



    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.cash = cash

    def description(self):
        id self.year >= 2021
          print(f'Модель: {self.model}, год выпуска: {self.yeat}, стоимость: {self.cash}, пробег: {self.odometr}')
        else:
          self.odometr = odometr
          print(f'Модель: {self.model}, год выпуска: {self.yeat}, стоимость: {self.cash}, пробег: {self.odometr}')

       def edit_odometr(self, km):
           self.odometr += km


class Battery
       def __init__(self, battery=75):
           self.battery = battery




       def describe_battery(self, battery=None):
          print(f'Мощность аккамультора: {self.battery} кВт')


class ElectricCar(Car)
    def __init__(self, model, year, cash):
        super().__init__(model, year, cash)

    def describe_battery(self, battery=None):
      if battery == True
        print(f'Мощность аккамультора: {self.battery} кВт')
          self.battery = 75

my_electric_car = ElectricCar('Testa', 2020, 40000)
my_electric_car.description(20000)
my_electric_car.describe_battery(150)



class Rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return str(self.width)

    def getArea(self):
        print(f'Площадь прямоугольника: {self.width} * {self.height} = {self.width * self.height}')


    def drawRect(self):

        print('*' * self.width)
        self.width -= 2
        for i in range(1, self.height-1):
            print('*', ' ' * self.width, '*')
        self.width += 1
            print('*' * self.width)




r1 = Rectangle(5, 3)
r1.getArea()
r1.drawRect()


# my_car = Car('BMW', 2015, 50000)
# my_car.description()
# my_car