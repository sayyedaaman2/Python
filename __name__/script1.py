# if __name__ == __main__ : (this script can be imported OR run standalone)
# Funcstions and classes in this module can be reused without the main block of code executing
# Food practice (code is modular,
#                helps readability,
#                leaves no global varibales,
#                avoid unintended execution)

#               Ex. library = import library for functionality
#                   When running library directly, display a help page

def favorite_food(food):
    print(f"Your favorite food is {food}")


def main():
    print("This is script1")
    favorite_food("Pizza")
    print("Goodbye!")
    
if __name__ == "__main__":
    main()
