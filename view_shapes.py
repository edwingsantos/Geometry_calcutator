from info import shapes_created

def view_shapes():
    if not shapes_created:
        print("No shapes.")
        return

    for i, s in enumerate(shapes_created):
        print(i, end=": ")
        s.display()