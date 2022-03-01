import math


class Polygon:
    
    def get_area(self):
        raise NotImplementedError

    def get_sides(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError


class Triangle(Polygon):
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a+self.b+self.c

    def get_sides(self):
        return [self.a, self.b, self.c]
    
    def get_area(self):
        semi_perimeter = (self.a + self.b + self.c) / 2
        return math.sqrt(
            semi_perimeter *
            (semi_perimeter - self.a) *
            (semi_perimeter - self.b) *
            (semi_perimeter - self.c)
        )


class Rectangle(Polygon):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height 

    def get_perimeter(self):
        return self.width*2 + self.height*2

    def get_sides(self):
        return [self.width, self.height, self.width, self.height]

    def get_area(self):
        return self.height*self.width



class Square(Rectangle):
    
    def __init__(self, length):
        self.length = length 
        self.width = self.length 
        self.height = self.length

    def get_area(self):
        return super().get_area()

    def get_sides(self):
        return super().get_sides()

    def get_perimeter(self):
        return super().get_perimeter()


s1 = Square(4)
print(s1.get_perimeter())