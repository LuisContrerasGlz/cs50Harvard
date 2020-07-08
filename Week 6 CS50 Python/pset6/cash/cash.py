#importing the CS50 Library to the program using the import command
from cs50 import get_float


#Asking the user for a valid input

while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break

#getting the cents and rounding the value with round fountion
cents = round(dollars * 100)

#store the coins in a coins variable
coins = 0

#setting the denominations in a list
denominations = [25, 10, 5, 1]

#substracting each time for each type of coin, when there is no way to substract one type it goes to the next one until you finish with the change
 
for denom in denominations:
    while cents >= denom:
        cents -= denom
        coins += 1

#print the coins    
print(coins)