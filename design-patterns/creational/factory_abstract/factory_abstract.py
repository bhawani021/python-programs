# Abstract shape classes
class Shape2DInterface(object):
    def draw(self):
        pass


class Shape3DInterface(object):
    def build(self):
        pass


# Concrete shape classes
class Circle(Shape2DInterface):
    def draw(self):
        print('Circle:Draw')


class Square(Shape2DInterface):
    def draw(self):
        print('Square:Draw')


class Sphere(Shape3DInterface):
    def build(self):
        print('Sphere:Build')


class Cube(Shape3DInterface):
    def build(self):
        print('Cube:Build')


# Abstract shape factory
class ShapeFactoryInterface(object):
    def get_shape(sides):
        pass


# Concrete shape factories
class Shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Circle()
        elif sides == 4:
            return Square()

        assert 0, 'Bad 2D shape creation: Shape not defined for ' + sides + ' sides'


class Shape3DFactory(ShapeFactoryInterface):
    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Sphere()
        elif sides == 4:
            return Cube()

        assert 0, 'Bad 3D shape creation: Shape not defied for ' + sides + ' faces'


if __name__ == '__main__':
    s1 = Shape2DFactory()
    s1.get_shape(1).draw()

    s2 = Shape3DFactory()
    s2.get_shape(4).build()
