from info import shapes, save_shapes

def sort_shapes():
    print("1 Area\n2 Perimeter")
    choice = input("Choose: ")

    if choice == "1":
        shapes.sort(key=lambda s: s.area())
    elif choice == "2":
        shapes.sort(key=lambda s: s.perimeter())

    save_shapes()
    print("Sorted!")