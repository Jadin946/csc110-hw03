"""
Name: Jadin Wilson
Peers: (add any collaborators)
References: stack overflow
"""

# imported modules
import statistics # let's us use mean, median, mode
import sys

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
#brings global grades into this function
    global grades
    
    for idx in range ( len(grades) ):
        # for each idx in 0, 1,... 4 do:

        while True:
            user_input = input("Give me the next grade in [0 to 10]:")
        # this checks if input is a digit
            if not user_input.isdigit():
                print("Error in read_five_ints: input string is not for an integer")
                sys.exit(1)
            num = int(user_input)
            # This checks if the input is within range
            if num > 10 or num<0:
                print("Error in read_five_ints: input integer outside of range")
                sys.exit(6)

            grades[idx] = num
            break


        # add the int to grades at index idx
    #Anything with this indentation is NO LONGER inside the loop


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    
    """
    global grades
    #asks for input
    pick_average = input("Pick 'a' for mean, 'b' for median, 'c' for mode: ")
    #if user picks a print and return avg
    if pick_average == "a":
        print("picked: Mean")
        avg = statistics.mean(grades)
        return avg
    #If user picks b print and return avg
    if pick_average == "b":
            print("picked: Median")
            avg = statistics.median(grades)
            return avg
    # If user picks c print and return avg
    if pick_average == "c":
        print("picked: Mode")
        avg = statistics.mode(grades)
        return avg
    # else print error and exit
    else:
        print("Error in pick_averaging_method: incorrect option picked")
        sys.exit(2)


# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    global grades
    #asks for input
    a = int(input("Pick '1' for print average, or '2' for plot average: "))
    # if input is 1 call print_list_and_average(average)
    if a == 1:
        print_list_and_average(average)
    # if a is equal to 2 call  plot_grades(average)
    elif a == 2:
        plot_grades(average)
    #otherwise print error and exit
    else:
    
        print("Error in pick_visualization: incorrect option picked")
        sys.exit(3)



# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
