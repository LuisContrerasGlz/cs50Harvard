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

#substracting each time for each type of coin, when there is no way to substract one type it goes to the next one until you finish with the change
while cents >= 25:
    cents -= 25
    coins += 1
    
while cents >= 10:
    cents -= 10
    coins += 1
    
while cents >= 5:
    cents -= 5
    coins += 1    
    
while cents >= 1:
    cents -= 1
    coins += 1    

#print the coins    
print(coins)