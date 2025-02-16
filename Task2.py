import uuid

class Figures():
    def __init__(self, id, x=0, y=0):
        self.x = x
        self.y = y
        self._id = id

    def get_id(self):
        return self._id

    def move(self, dx, dy):
        try:
            self.x += dx
            self.y += dy
        except TypeError:
            print("Значение должно быть числом. Фигура не была перемещена.")
        else:
            print(f"Вы переместили фигуру {self._id} на новую позицию: ({self.x},{self.y}).")

    def __str__(self):
        return f"Фигура с ID {self._id}"

class Triangle(Figures):
    def __init__(self, side_a, height):
        super().__init__(str(uuid.uuid4()))
        self.height = height
        self.side_a = side_a

    def area(self):
        try: 
            return 0.5 * self.height * self.side_a
        except TypeError:
            print("Площадь невозможно посчитать. Одно или несколько значений не являются числами.")
            return
    
class Rectangle(Figures):
    def __init__(self, side_a, side_b):
        super().__init__(str(uuid.uuid4()))
        self.side_a = side_a
        self.side_b = side_b

    def area(self): 
        try: 
            return self.side_a * self.side_b
        except TypeError:
            print("Площадь невозможно посчитать. Одно или несколько значений не являются числами.")
            return
    
def Compare(figure1, figure2):
    area1 = figure1.area()
    area2 = figure2.area()

    if area1 is None or area2 is None:
        print("Сравнение невозможно, так как площадь не была подсчитана.")
        return

    if area1 > area2:
        return f"Фигура {figure1.get_id()} больше по площади, чем фигура {figure2.get_id()}"
    elif area2 > area1:
        return f"Фигура {figure1.get_id()} меньше по площади, чем фигура {figure2.get_id()}"
    else:
        return f"Фигура {figure1.get_id()} равна по площади фигуре {figure2.get_id()}"

triangle = Triangle(side_a="f", height=4)
rectangle = Rectangle(side_a=4, side_b=5)

print(triangle)
print(rectangle)

print(Compare(triangle, rectangle))

triangle.move(1, 2)
rectangle.move(0,-1)

triangle.move(1, 2)
rectangle.move(5, "a")