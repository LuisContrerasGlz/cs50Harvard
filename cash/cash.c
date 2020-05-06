//Including the libraries in able to use the code in the program
#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    double change;
    //Aks user for how much change we own him, 
    //If user mentions a negative number ask user to select again since it is invalid selection
    do
    {
        change = get_double("How much do I own you sir?\n");
    }
    while (change < 0);
    
   //Converting dollars to cents
   int cents = round(change * 100);
   int coins = 0;
   
   //Option 1, whiles.
   //Check if the 25 cent is possible to use and repeat until is not possible to use
   while (cents >= 25)
   {
       cents -= 25;
       coins++;
   }
   //Check if the 10 cent is possible to use and repeat until is not possible to use
   while (cents >= 10)
   {
       cents -= 10;
       coins++;
       
   }
   //Check if the 5 cent is possible to use and repeat until is not possible to use
   while (cents >= 5)
   {
       cents -= 5;
       coins++;
       
   }
   //Check if the 5 cent is possible to use and repeat until is not possible to use
   while (cents >= 1)
   {
       cents -= 1;
       coins++;
       
   }
    printf("%i\n", coins);
}
