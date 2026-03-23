#ES 1rst geomarty calculator

#import the files 
import create_shapes
import view_shapes
import select_shapes
import compare_shapes
import sort_shapes
import formula_guide

#print the greating
print("GEOMETRY CALCULATOR\N WELCOME TO THE SHAPE CALCULATOR!") 

#make a funtion for main 
def main():
    #print that this is the main funtion 
    print("Main Function")
    #make a while true loop 
    while True:
        #print the amount of shpaes created 
    
    




    
        #Input the different actions the user can choose from called choice
        choice = input("1: Create New Shape\n2: View All Shapes\n3: Select Shape\n4: Compare Shapes\n5: Sort Shapes\n:6 Formula Guide\n:7 Quit").strip()
        #if choice equals 1 call the create shape funtion 
        if choice == "1":
            create_shapes()
        #elif choice equlas 2 call the view shapes funtion 
        elif choice == "2":
            view_shapes()
        #elif choice equals 3 call the select shapes funtion
        elif choice == "3":
            select_shapes()
        #elif choice equals 4 call the compare funtion
        elif choice == "4":
            compare_shapes()
        #elif chioce equlas 5 call the sort funtion
        elif choice == "5":
            sort_shapes()
        #elif choice equals 6 call the formula guide funtion 
        elif choice == "6":
            formula_guide()
        #elif choice equals 7 break the loop 
        elif choice == "7":
            break 
        #else print that the option is not there and continue
        else:
            print("Option not avialable, please try agian.")
            continue


