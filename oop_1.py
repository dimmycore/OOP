class Rectangle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle:{self.x},{self.y},{self.width},{self.height}.'

    def get_area(self):
        return self.width*self.height

rect_1=Rectangle(5,10,50,100)
print(rect_1)
print(type(rect_1))
print(rect_1.get_area())

#пишем код для описания геометрической фигуры.
#создаём класс «прямоугольник» с помощью магического метода init(). На выходе в консоли получаем площадь данной фигуры.
# при помощи магического метода __str__ возвращаем атрибуты прямоугольника как строку.
# объект - прямоугольник со значениями атрибута x = 5, y = 10, width = 50, height = 100
