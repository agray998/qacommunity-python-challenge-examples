class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect1 = Rectangle(5, 3)
    rect2 = Rectangle(7, 10)
    print(rect1.area())
    print(rect2.area())