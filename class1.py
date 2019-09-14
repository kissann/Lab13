#Задача 1
#Розробити класс Sphere для представлення сфери у тривимірному просторі.

#конструктор, який приймає 4 дійсних числа: радіус, та 3 координати центру кулі.
# Якщо конструктор викликається без аргументів, створити об'єкт сфери із одиничним радіусом та центром у початку координат.
# Якщо конструктор викликається з 1 аргументом, створити об'єкт сфери з відповідним радіусом та центром у початку координат.
from math import *
class Spheres:
    def __init__(self, radius=0,x=0,y=0,z=0):
        self.radius = radius
        self.area = 0
        self.volume = 0
        self.zentr=0
        self.x=x
        self.y=y
        self.z=z

    def get_radius(self):
        return self.radius

    def get_square(self):
        r = int(self.radius)
        self.area = 4 * 3.14 * (r * r)
        return (self.area)

    def get_volume(self):
        r = int(self.radius)
        self.volume = (4 / 3) * 3.14 * (r * r * r)
        return (self.volume)

    def get_center(self):
        self.zentr="x= "+str(self.x)+"см; y="+str(self.y)+"см;z="+str(self.z)+"см"
        return (self.zentr)
    def set_radius(self,r):
        self.radius=r
    def set_center(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def is_point_inside(self,x,y,z):
        DlinaV = sqrt((int(self.x)-int(x))*(int(self.x)-int(x))+(int(self.y)-int(y))*(int(self.y)-int(y))+(int(self.z)-int(z))*(int(self.z)-int(z)))
        if DlinaV<int(self.radius):
            print("Входит")
        else:
            print("Не входит")

def main():
    flag=True
    r = input("Введите радиус сферы: ")
    x = input("Введите x=")
    y = input("Введите y=")
    z = input("Введите z=")
    s = Spheres(r, x, y, z)
    r1=r
    x1=x
    y1=y
    z1=z
    while flag:
       n=input("Что вы хотите: Площадь-ar; Объем - v; Изменить радиус - chr; Проверить точку - tch; Получить радиус - getr; Изменить координаты - chx; Выйти - ^")
       if(n=="ar"):

            print("Площадь поверхности сферы: ", s.get_square())
       elif(n=="v"):
           print("объем сферы: ", s.get_volume())
       elif(n=="tch"):

           x1=input("х точки = ")
           y1 = input("y точки = ")
           z1 = input("z точки = ")
           s.is_point_inside(x1, y1, z1)
       elif (n == "chr"):

           r1=input("Введите новый радиус")
           s = Spheres(r1, x1, y1, z1)
           r1=r1

       elif (n == "getr"):
          print(s.radius)
       elif (n == "chx"):
           x1 = int(input("Введите x"))
           y1 = int(input("Введите y"))
           z1 = int(input("Введите z"))

           s = Spheres(r1, x1, y1, z1)


main()