#ES info, remember shapes stored here or start to 

#import things that are necessary 
import csv
from shapes import Circle, Rectangle, Square, Triangle

#make shapes a list 
shapes_created = []

#make a funtion for 
def load_shapes():
    try:
        file = open("shapes.csv", "r")
        reader = csv.reader(file)

        for row in reader:
            if row[0] == "Circle":
                shapes_created.append(Circle(float(row[1])))

            elif row[0] == "Rectangle":
                shapes_created.append(Rectangle(float(row[1]), float(row[2])))

            elif row[0] == "Square":
                shapes_created.append(Square(float(row[1])))

            elif row[0] == "Triangle":
                shapes_created.append(Triangle(float(row[1]), float(row[2]), float(row[3]), float(row[4])))

        file.close()

    except:
        file = open("shapes.csv", "w")
        file.close()


def save_shapes():
    file = open("shapes.csv", "w", newline="")
    writer = csv.writer(file)

    for s in shapes_created:
        if isinstance(s, Circle):
            writer.writerow(["Circle", s.radius])

        elif isinstance(s, Rectangle):
            writer.writerow(["Rectangle", s.length, s.width])

        elif isinstance(s, Square):
            writer.writerow(["Square", s.side])

        elif isinstance(s, Triangle):
            writer.writerow(["Triangle", s.base, s.height, s.side1, s.side2])

    file.close()