import math


class Figure_square:
    def __init__(self):
        pass
    def circle_square(self, radius):
        #Проверка на неотрицательность радиуса
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return (round(radius ** 2 * math.pi, 2))
       
    def triangle_square(self, side1, side2, side3):
        
        #Проверка на неотрицательность сторон
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Стороны треугольника должны быть положительными")
        

        #Проверка на то, что стороны образуют треугольник
        if (side1 + side2 <= side3 or 
            side1 + side3 <= side2 or 
            side2 + side3 <= side1):
            raise ValueError("Стороны не образуют треугольник")
        
        #Расчет площади по формуле Герона
        semiperimeter = (side1 + side2 + side3) / 2
        return math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter- side3)) 
    
    def is_rectangular(self, side1, side2, side3):
        #Проверка на неотрицательность сторон
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Стороны треугольника должны быть положительными")
        

        #Проверка на то, что стороны образуют треугольник
        if (side1 + side2 <= side3 or 
            side1 + side3 <= side2 or 
            side2 + side3 <= side1):
            raise ValueError("Стороны не образуют треугольник")

        sides = sorted([side1, side2, side3])

        
        
        if (sides[2]**2) == (sides[0]**2 + sides[1]**2):
            return "Треугольник прямоугольный"
        else:
            return "Треугольник не прямоугольный"
        

def circle_square(radius):
    return Figure_square().circle_square(radius)

def triangle_square(side1, side2, side3):
    return Figure_square().triangle_square(side1, side2, side3)

def is_rectangular(side1, side2, side3):
    return Figure_square().is_rectangular(side1, side2, side3)

