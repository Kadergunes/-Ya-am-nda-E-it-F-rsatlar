class Animal:
    def speak(self):
        print('Hayvan ses çıkarıyor.')


class Dog(Animal):
    def speak(self):
        print('Hav! Hav!')


class Cat(Animal):
    def speak(self):
        print('Miyav!')



animal = Animal()
animal.speak()


dog = Dog()
dog.speak()

cat = Cat()
cat.speak()


#ornek2


class Shape:
    def area(self):
        pi=3.14
        print('İşleminiz yapılıyor')

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def print_area(shape):
    print(f'{shape.__class__.__name__} alanı: {shape.area()}')


rect = Rectangle(5, 10)
circle = Circle(7)
triangle = Triangle(6, 8)


print_area(rect)
print_area(circle)
print_area(triangle)

