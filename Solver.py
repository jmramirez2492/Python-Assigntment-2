import Shapes3d
import csv

class Solver:
    total = 0
    shapes = []

    with open("exampleInput.csv", mode='r') as file:
        csvFile = csv.reader(file, delimiter=',')
        for lines in csvFile:
            if lines[0] == "cube":
                shapes.append(Shapes3d.Cube(float(lines[1])))
            elif lines[0] == "cuboid":
                shapes.append(Shapes3d.Cuboid(float(lines[1]), float(lines[2]), float(lines[3])))
            elif lines[0] == "sphere":
                shapes.append(Shapes3d.Sphere(float(lines[1])))
            elif lines[0] == "cylinder":
                shapes.append(Shapes3d.Cylinder(float(lines[1]), float(lines[2])))
            elif lines[0] == "prism":
                shapes.append(Shapes3d.Prism(float(lines[1]), float(lines[2]), float(lines[3])))
            elif lines[0] == "area":
                for shape in shapes:
                    total += sum(calc.GetSurfaceArea() for calc in shapes) * float(lines[1])
                    shapes = []
                shapes.clear()
            elif lines[0] == "volume":
                for shape in shapes:
                    total += sum(calc.GetVolume() for calc in shapes) * float(lines[1])
                    shapes = []
                shapes.clear()
    print(total)