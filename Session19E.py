import math

class Point:

    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def show(self):
        print("Point {} is: {}|{}".format(self.label, self.x, self.y))


    # self is reference to the object
    # def create_points_from_file(self):

    # Annotation : classmethod shall pass reference to class rather than object
    @classmethod
    def create_points_from_file(cls):
        # cls is reference to the Class. It comes only if annotation @classmaethod is used :)
        print("cls is:", cls)
        print("cls contains:", cls.__dict__)

        file = open("points.csv", "r")
        lines = file.readlines()

        points = []

        lbl = 1
        for line in lines:
            point = line.split(",")
            # cls() -> is execution of __init__() constructor and we will get the object in return
            # refToObject = cls(float(point[0]), float(point[1]), "P{}".format(lbl))

            points.append(cls(float(point[0]), float(point[1]), "P{}".format(lbl)))
            lbl += 1

        return points

    # Annotation : staticmethod shall not pass reference to class or object
    # we have staticmethod which can be used with class name but it will not have any reference to class or object
    # it is just a simple function fo dosing some algorithmic computation may be :)
    @staticmethod
    def create_points():
        file = open("points.csv", "r")
        lines = file.readlines()

        points = []

        lbl = 1
        for line in lines:
            point = line.split(",")
            # pRef = Point(float(point[0]), float(point[1]), "P{}".format(lbl))
            # points.append(pRef)
            points.append(Point(float(point[0]), float(point[1]), "P{}".format(lbl)))
            lbl += 1

        return points


    def calculate_distance(point1, point2): # point1 acts as self
        distance = math.sqrt((point2.y - point1.y)**2 + (point2.x - point1.x)**2)
        return distance

    @staticmethod
    def calculate_distance_again(point1, point2): # point1 and point2 are just 2 inputs
        distance = math.sqrt((point2.y - point1.y)**2 + (point2.x - point1.x)**2)
        return distance



def main():
    p1 = Point(10, 20, "A")
    p2 = Point(11, 22, "B")

    p1.show()
    p2.show()

    print("Point is:", Point)
    print("Point contains:", Point.__dict__)

    print()

    # class methods are executed with class name :)
    # they take reference of class i.e. cls which can be any name of our choice as 1st input
    # points = Point.create_points_from_file()

    points = Point.create_points()
    for point in points:
        point.show()


    print()
    distance = Point.calculate_distance(p1, p2)
    print("distance is:", distance)

    print()

    distance = Point.calculate_distance_again(p1, p2)
    print("distance is:", distance)


if __name__ == '__main__':
    main()
