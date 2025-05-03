# внедряем модуль/библиотеку turtle для работы
import turtle
# внедряем модуль/библиотеку math для работы c PI
import math

# указываем тело и скорость, того с чем рисуем
turtle.shape("turtle")
turtle.speed(4)

# функция, чтобы рисовать квадрат по его стороне
def draw_rectangle(size:float):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

# функция, чтобы рисовать равносторонний треугольник по его стороне
def draw_ptriangle(size:float):
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

# функция, чтобы рисовать окружность по его радиусу
def draw_circle(radius:float):
    x = (2 * radius * math.pi) / 360
    for i in range(360):
        turtle.forward(x)
        turtle.left(1)

# вызываем функцию, рисуем квадрат со стороной 100
draw_rectangle(100) 
# вызываем функцию, рисуем правильный треугольник со стороной 100
draw_ptriangle(100) 
# вызываем функцию, рисуем окружность со радиусом 100
draw_circle(100)