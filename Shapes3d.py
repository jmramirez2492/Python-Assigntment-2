import Shapes
import math

# Cuboid Class
class Cuboid:
    def __init__(self, width, height, length):
        self._width = width
        self._height = height
        self._length = length

    def GetSurfaceArea(self):
        return 2 * ((self._length * self._height) + (self._width * self._height) + (self._length * self._width))

    def GetVolume(self):
        return self._width * self._length * self._height


# Cube Class (child of cuboid)
class Cube(Cuboid):
    def __init__(self, Length):
        # Reference the parent class with super 'special'
        super().__init__(Length, Length, Length)


# Cylinder Class
class Cylinder:
    def __init__(self, radius, height):
        self._height = height
        self._base = Shapes.Circle(radius)

        self._surfaceArea = self._GetSurfaceArea()
        self._volume = self._GetVolume()

    def _GetSurfaceArea(self):
        baseArea = self._base.GetArea()
        faceArea = self._base.GetPerimeter() * self._height

        return (baseArea * 2) + faceArea

    def _GetVolume(self):
        return self._base.GetArea() * self._height

    def GetSurfaceArea(self):
        return self._surfaceArea

    def GetVolume(self):
        return self._volume
 

# Sphere Class
class Sphere:
    def __init__(self, radius):
        self._radius = radius

    def GetSurfaceArea(self):
        # double ** raises to power
        return (4 * math.pi * (self._radius ** 2))

    def GetVolume(self):
        return ((4/3) * math.pi * (self._radius ** 3))


#N-gonal prism
class Prism:
    def __init__(self, sides, sideLength, height):
        self._height = height
        self._base = Shapes.Polygon(sides, sideLength).GetArea()
        self._perimeter = Shapes.Polygon(sides, sideLength).GetPerimeter()

    def GetSurfaceArea(self):
        return (self._perimeter * self._height) + (2 * self._base)
    
    def GetVolume(self):
        return self._base * self._height