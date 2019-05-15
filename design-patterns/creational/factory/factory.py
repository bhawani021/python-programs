class Shape(object):
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Circle:Draw")


class Square(Shape):
    def draw(self):
        print("Square:draw")


class Rectangle(Shape):
    def draw(self):
        print("Rectangle:draw")


class ShapeFactory(object):
    @staticmethod
    def get_shape(obj_type):
        if obj_type == 'circle':
            return Circle()
        elif obj_type == 'square':
            return Square()
        elif obj_type == 'rectangle':
            return Rectangle()

        raise Exception('Could not find share {}'.format(obj_type))


if __name__ == '__main__':
    shape = ShapeFactory.get_shape('circle')
    shape.draw()

    shape = ShapeFactory.get_shape('rectangle')
    shape.draw()

    shape = ShapeFactory.get_shape('triangle')
    shape.draw()