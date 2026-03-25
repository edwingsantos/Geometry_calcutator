#ES view shapes

#import needed things
from info import shapes_created

#make a funtion for viewing shapes
def view_shapes():
    #if there is not shapes print to shapes and return
    if not shapes_created:
        print("No shapes")
        return
    #enumerate the shapes with a loop and print them 
    for i, s in enumerate(shapes_created):
        print(i, end=": ")
        s.display()