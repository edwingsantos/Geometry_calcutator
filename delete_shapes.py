from info import shapes_created, save_shapes

def delete_shapes():
    if not shapes_created:
        print("No shapes to delete.")
        return

    # show shapes
    for i, s in enumerate(shapes_created):
        print(i, end=": ")
        s.display()

    try:
        index = int(input("Enter index to delete: "))

        if index < 0 or index >= len(shapes_created):
            print("Invalid index.")
            return

        shapes_created.pop(index)
        save_shapes()     

        print("Shape deleted!")

    except:
        print("Error deleting shape.")