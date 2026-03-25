#ES 1rst main 
#call all of the functions from their repective files
from create_shapes import create_shapes
from view_shapes import view_shapes
from delete_shapes import delete_shapes
from compare_shapes import comparing
from sort_shapes import sort_shapes
from formula_guide import formula_guide
from info import load_shapes

#make a funtion for main 
def main(): 
    #print a welcome messege and print the shapes for the user to see
    print("Welcome to the geometric calculator")
    load_shapes()
    #make a while true loop asking the user what they want to do 
    while True:
        choice = input("\n1 Create\n2 View\n3 delete\n4 Compare\n5 Sort\n6 Formulas\n7 Quit\nChoice:")
        #If choice is 1 call the create shapes 
        if choice == "1":
            create_shapes()
        #If choice is 2 call the view shapes
        elif choice == "2":
            view_shapes()
        #If choice is 3 call the select shapes
        elif choice == "3":
            #I didnt see a reason to select a shape and do nothing so I decided to delete shapes
            delete_shapes()
        #If choice is 4 call the compare shapes
        elif choice == "4":
            comparing()
        #If choice is 5 call the sort shapes
        elif choice == "5":
            sort_shapes()
        #If choice is 6 call the formula guide
        elif choice == "6":
            formula_guide()
        #if choice is 7 break 
        elif choice == "7":
            break
        #else print invalid option select again
        else:
            print("Invalid option please select again")

#call main
    main()