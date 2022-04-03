# class Dog:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def sit(self):
#         """Собака садиться по команде"""
#         print(f'{self.name} сел в тюрьму')
#
#     def run(self):
#         print(f'{self.name} убежал')
#
#     def get_info(self):
#         print(f'Имя: {self.name}\nВозраст: {self.age}')
#
#
# my_pet =Dog('Bobik', 2)
# my_pet.sit()
# my_pet.run()
# my_pet.get_info()
#
# my_pet_2 = Dog('Jorik')
# my_pet_2.run(self)
# my_pet_2.get_info()

# class Restaraunt:
#     def __init__(self, restoraunt_name, cuisine_type):
#         self.name = restoraunt_name
#         self.cuisine = cuisine_type
#
#     def describe_restaraunt(self):
#         print('Название ресторана: {self.name}')
#
#     def open_restaraunt(self):
#         print(f'Ресторан {self.name} открыт')
#
#     def cuisine(self):
#         print(f'Блюдо: {self.cuisine}')
#
#
# info = Restaraunt('KFC,' 'Нагетсы')
# info.describe_restaraunt()
# info.open_restaraunt()
# info.cuisine()
#

import pygame as pg
import sys

width_rect = 200
height_rect = 100
window_width = 600
window_height = 400
white = 255, 255, 255
black = 0, 0, 0
green = 0, 255, 0
blue = 0, 255, 255
yellow = 255, 255, 0


x, y = 100, 200

screen = pg.display.set_mode((window_width, window_height))
clock = pg.time.Clock()

pg.display.set_caption('Моя программа')























screen = pg.display.set_mode((window_width, window_height))


while True:
     for i in pg.event.get():
          if i.type == pg.QUIT:
               sys.exit()

"""Отрисовка прямоугольников"""

pg.draw.rect(screen, (255, 0 ,20), (window_width // 2 - 100, window_height // 2 - 50, 200, 100))
pg.draw.rect(screen, (100, 200, 20), (window_width // 2 - 100, window_height // 2 - 50 + 110, 200, 100), 10)

"""Отрисовка линий"""

 # pg.draw.line(screen, white, (0, 0), (600, 400), 10)
 # pg.draw.aaline(screen, white, (10, 70), (290, 255))
#     pg.draw.line(screen, white, (0, 0), (600, 400), 10)
#     pg.draw.line(screen, white, (600, 0), (0, 400), 10)






# pg.draw.circle(screen, yellow, (window_width // 2, window_height // 2), r)
#
# clock.tick(FPS)
# screen.fill(white)
#
# pg.draw.circle(screen, yellow, (x, y), r)
#
# x += direct_x
# if x >= window_width or x < 0:
#      direct_x = -direct_x

"""Отрисовка кругов"""

# clock.tick(FPS)
# screen.fill(white)
#
# pg.draw.circle(screen, yellow, (x, y), r)
#
# x += direct_x
# if x >= window_width or x < 0:
#      direct_x = -direct_x


pg.display.update()







































