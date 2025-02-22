import uuid

class Figure():
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
        self._id = str(uuid.uuid4())

    def get_id(self):
        return self._id

    def get_position(self):
        return self._x, self._y
    
    def move(self, dx, dy):
        self._x += dx
        self._y += dy
        print(f"Вы переместили фигуру {self._id} на новую позицию: ({self._x}, {self._y}).")

    def __str__(self):
        return f"Фигура с ID {self._id}"

class Triangle(Figure):
    def __init__(self, side_a, height, x=0, y=0):
        super().__init__(x, y)
        self._height = height
        self._side_a = side_a

    def area(self):
        return 0.5 * self._height * self._side_a

class Rectangle(Figure):
    def __init__(self, side_a, side_b, x=0, y=0):
        super().__init__(x, y)
        self._side_a = side_a
        self._side_b = side_b

    def area(self): 
        return self._side_a * self._side_b

def compare(figure1: Figure, figure2: Figure) -> str:
    area1 = figure1.area()
    area2 = figure2.area()

    if area1 > area2:
        return f"Фигура {figure1.get_id()} больше по площади, чем фигура {figure2.get_id()}"
    elif area2 > area1:
        return f"Фигура {figure1.get_id()} меньше по площади, чем фигура {figure2.get_id()}"
    else:
        return f"Фигура {figure1.get_id()} равна по площади фигуре {figure2.get_id()}"

triangle = Triangle(side_a=5, height=4)
rectangle = Rectangle(side_a=4, side_b=5)

print(triangle)
print(rectangle)
print(compare(triangle, rectangle))

triangle.move(1, 2)
rectangle.move(0, -1)

triangle.move(1, 2)
rectangle.move(5, 4)
