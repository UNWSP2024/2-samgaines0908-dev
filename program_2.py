    #Author: Sam Gaines
    #Date: 1/30/2026
    #Title: Average age
def average_age():
    #Get User Input
    age1 = int(input("Enter your age friend 1: "))
    age2 = int(input("Enter your age friend 2: "))
    age3 = int(input("Enter your age friend 3: "))
    age4 = int(input("Enter your age friend 4: "))
    age5 = int(input("Enter your age friend 5: "))
    #Sum ages
    sum_of_age= age1+age2+age3+age4+age5
    # Average the ages
    average_age = sum_of_age/5.0
    # Print the results
    print("The average age of your friends is:",average_age)
    # Line which calls the above function.
average_age()
