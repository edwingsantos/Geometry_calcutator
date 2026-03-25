#ES 1rst compare shapes

#call all of the funtions needed
from info import shapes_created
from view_shapes import view_shapes

#print the shpaes so user can see them 
print(view_shapes)
#make a funtion for comparing shapes
def comparing():
    #make a while loop and if there is less than two shapes return 
    while True:
        if len(shapes_created) < 2:
            print("Need 2 shapes.")
            return

        #ask the user to put the numbers to compare
        try:
            shape1 = int(input("First shape: "))
            shape2 = int(input("Second shape: "))

            s1 = shapes_created[shape1]
            s2 = shapes_created[shape2]
            #if the area of shape one is grater than two then print shape one is biger area
            if s1.area() > s2.area():
                print("Shape 1 bigger area")
            #else print that the are of 2 is bigger
            else:
                print("Shape 2 bigger area")
            #repeat for perimeter
            if s1.perimeter() > s2.perimeter():
                print("Shape 1 bigger perimeter")
            else:
                print("Shape 2 bigger perimeter")
        #else print that the options were not avilabe and to select agian,continue 
        except:
            print("Please select numbers listed")
            continue