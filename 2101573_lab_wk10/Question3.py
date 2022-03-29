# Lab 1 Question 2B:
def findModule(moduleCode):
    switcher = {
        "CSC1006": "Mathematics 2",
        "CSC1007": "Operating Systems",
        "CSC1008": "Data Structure and Algorithms",
        "CSC1009": "Object Oriented Programming",
        "CSC1010": "Computer Networks"
    }
    return switcher.get(moduleCode, "nothing")


# Main method
if __name__ == '__main__':
    # User to input module code
    moduleCode = input("Enter module code: ")

    # Call method to find module by module code and return value
    # upper() to convert string to uppercase
    print("Module: " + str(findModule(moduleCode.upper())))

    # Lab 1 Question 2C:
    print("Value of x : ")
    # For loop to run from value 102 to 65
    for x in range(102, 65, -1):
        # Use % in if statement to check if value is odd
        if x % 2 == 1:
            # Run this statement when value is odd
            print(x)
