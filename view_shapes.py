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
    for i in enumerate(shapes_created, 1):
        print(f"{i}")
#print the options enumerated
for i, shapes_created in enumerate(shapes_created,1):
    print(f"Shape: {shapes_created}")
