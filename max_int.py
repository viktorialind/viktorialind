#first i set the counter =0 
#my next step is to go in to while loop
#my while loop works until the input is negative
#when the input is negative it prints the highest number ,max_int
num_int = int(input("Input a number: "))   
max_int =0

while num_int >=0:
    if max_int<num_int:
       max_int = num_int
    num_int = int(input("Input a number: ")) 

print("The maximum is", max_int) 