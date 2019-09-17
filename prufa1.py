my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
if my_int % 2 == 0:
        my_int = int(my_int / 2)
        bin_str = 1
        print("The remainder is:", 0)
       
elif my_int % 2 == 1:
        my_int = int(my_int / 2)
        bin_str = 1
        print("The remainder is:", 1)
      
print("The binary of", my_int, "is", bin_str)
