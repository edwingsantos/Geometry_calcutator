#Es sort shapes

#call all funtions needed
from info import shapes_created, save_shapes
#make a funtion for sorting things
def sort_shapes():
    #print the area and perimeter and make user choose with input
    print("1 Area\n2 Perimeter")
    choice = input("Choose: ")
    #if choice is one the sort the shapes by area 
    if choice == "1":
        shapes_created.sort(key=lambda s: s.area())
    #if choice is two then sort the shapes by perimeter
    elif choice == "2":
        shapes_created.sort(key=lambda s: s.perimeter())