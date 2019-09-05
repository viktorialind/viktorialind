#first I ask for an input for the length of sequence
# I then make 3 three numbers, counter and a variable for the sum
#my next step is to go in a while loop that will test if the counter is < n the input
# I make a variable that will sum the 3 numbers
#next I want to print the sum 
#than I will test the 3 numbers
# and add 1 to the counter for the interation




n = int(input("Enter the length of the sequence: "))  
num_one = 1
num_two = 0
num_three = 0
counter = 0
sum_int = 0
while counter < n:
    sum_int = num_one + num_two + num_three
    print(sum_int)
    if num_one >= 2:
        num_three = num_two
    num_two = num_one
    num_one = sum_int
    counter += 1