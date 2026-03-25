from info import shapes, save_shapes

def delete_shapes():
    if not shapes:
        print("No shapes to delete.")
        return

    # show shapes
    for i, s in enumerate(shapes):
        print(i, end=": ")
        s.display()

    try:
        index = int(input("Enter index to delete: "))

        if index < 0 or index >= len(shapes):
            print("Invalid index.")
            return

        shapes.pop(index)   # remove shape
        save_shapes()       # update CSV

        print("Shape deleted!")

    except:
        print("Error deleting shape.")