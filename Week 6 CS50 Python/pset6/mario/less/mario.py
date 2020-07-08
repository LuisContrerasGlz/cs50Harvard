#importing the CS50 Library to the program using the import command
from cs50 import get_int

#Asking the user for a valid input for the piramid height

while True:
    n = get_int("Height: ")
    if n >=1 and n <=8:
        break
    
    
#Priting the pyramid checking for blank spaces first and then puting the hash

for i in range(n):
    
    print((n - 1 -i) * " ", end="" )
    print((i + 1) * "#")