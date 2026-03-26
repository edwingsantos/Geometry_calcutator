#ES create shpaes

#import all things needed 
from shapes import Circle, Rectangle, Square, Triangle
from info import shapes_created, save_shapes

#make a funtion for create shapes
def create_shapes():
    while True:
        #print the choice and input makeing user choose 
        print("\n1 Circle\n2 Rectangle\n3 Square\n4 Triangle")
        choice = input("Choose: ")
        #if choice is 1 make r be radius and append it to cirlce 
        if choice == "1":
            r = float(input("Radius: "))
            shapes_created.append(Circle(r))
            #call save shpaes 
            save_shapes()
            return
        #if choice is 2 ask the user for lenght and width and append it to rectangle 
        elif choice == "2":
            l = float(input("Length: "))
            w = float(input("Width: "))
            shapes_created.append(Rectangle(l, w))
            #call save shpaes 
            save_shapes()
            return
        #if user is 3 ask for the side and append it to square 
        elif choice == "3":
            s = float(input("Side: "))
            shapes_created.append(Square(s))
            #call save shpaes 
            save_shapes()
            return
        #if choice is 4 ask for the details and append it to traingle
        elif choice == "4":
            b = float(input("Base: "))
            h = float(input("Height: "))
            s1 = float(input("Side1: "))
            s2 = float(input("Side2: "))
            shapes_created.append(Triangle(b, h, s1, s2))
            #call save shpaes 
            save_shapes()
            return
        #else print to select an acutal option
        else:
            print("select an actua option")
            continue
