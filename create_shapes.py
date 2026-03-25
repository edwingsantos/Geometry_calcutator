#ES create shpaes


from shapes import Circle, Rectangle, Square, Triangle
from info import shapes_created, save_shapes

def create_shapes():
    print("\n1 Circle\n2 Rectangle\n3 Square\n4 Triangle")
    choice = input("Choose: ")

    try:
        if choice == "1":
            r = float(input("Radius: "))
            shapes_created.append(Circle(r))

        elif choice == "2":
            l = float(input("Length: "))
            w = float(input("Width: "))
            shapes_created.append(Rectangle(l, w))

        elif choice == "3":
            s = float(input("Side: "))
            shapes_created.append(Square(s))

        elif choice == "4":
            b = float(input("Base: "))
            h = float(input("Height: "))
            s1 = float(input("Side1: "))
            s2 = float(input("Side2: "))
            shapes_created.append(Triangle(b, h, s1, s2))

        save_shapes()
        print("Saved!")

    except:
        print("Error")