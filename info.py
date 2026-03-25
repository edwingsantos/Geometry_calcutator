#ES info, remember shapes stored here or start to 

#import things that are necessary 
import csv
from shapes import Circle, Rectangle, Square, Triangle

#make shapes a list 
shapes_created = []

#make a funtion for 
def load_shapes():
    try:
        #make file be the relative path to the csv file 
        file = open("shapes.csv", "r")
        #make reader be csv reader of the file 
        reader = csv.reader(file)
        #make a loop for fow in reader 
        for row in reader:
            #if the row 0 to be circle
            if row[0] == "Circle":
                #append to the shapes created list 
                shapes_created.append(Circle(float(row[1])))
            #make the same thing but for rectangle, square and triangle 
            elif row[0] == "Rectangle":
                shapes_created.append(Rectangle(float(row[1]), float(row[2])))

            elif row[0] == "Square":
                shapes_created.append(Square(float(row[1])))

            elif row[0] == "Triangle":
                shapes_created.append(Triangle(float(row[1]), float(row[2]), float(row[3]), float(row[4])))
        #close the file 
        file.close()
    #else make file open the csv file write and close it 
    except:
        file = open("shapes.csv", "w")
        file.close()

#Make a funtion for save shapes 
def save_shapes():
    #make file open the csv file 
    file = open("shapes.csv", "w", newline="")
    #make a writer be csv writer to the file 
    writer = csv.writer(file)
    #for s in shapes created 
    for s in shapes_created:
        #if being in circle is true then write the radius on the csv file
        if isinstance(s, Circle):
            writer.writerow(["Circle", s.radius])
        #reapeat for rectangle,square,trainge
        elif isinstance(s, Rectangle):
            writer.writerow(["Rectangle", s.length, s.width])

        elif isinstance(s, Square):
            writer.writerow(["Square", s.side])

        elif isinstance(s, Triangle):
            writer.writerow(["Triangle", s.base, s.height, s.side1, s.side2])

    file.close()