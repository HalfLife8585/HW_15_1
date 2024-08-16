import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        total_area = self.get_square() + other.get_square()
        new_width = 1
        new_height = total_area
        for i in range(1, int(math.sqrt(total_area)) + 1):
            if total_area % i == 0:
                new_width = i
                new_height = total_area // i
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        new_area = self.get_square() * n
        new_width = 1
        new_height = new_area
        for i in range(1, int(math.sqrt(new_area)) + 1):
            if new_area % i == 0:
                new_width = i
                new_height = new_area // i
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Тести
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("Всі тести пройдено успішно!")
