#The player starts in square (1,1)
#We will start by assigning x and y its first coordinates
#We need four functions to define when we can move from one square to another
#We need to make a function to define the possibilites the user could take and we use strings
#We make a function that asks the user for an input on which direction he chooses
#We make a function that returns 1 if true and 0 if false
#We make a function to define the value of x and y that corresponds to the movements
#Now we have made all the functions required and start on the main code
#The main code starts with a while loop and continous until the user reaches the victory square

x,y = 1,1



def north(x,y):

    if y == 3 or (x,y) == (2,2) or (x,y) == (3,1):

        return False

    return True



def east(x,y):

    if (x,y) != (1,2) and (x,y) != (1,3) and (x,y) != (2,3):

        return False

    return True
