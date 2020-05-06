//Including the libraries in able to use the code in the program
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    int space;
    //Aks user for the number of # wanted, 
    //If height is less than 1 or greater than 8 (or not an integer at all), ask user to select again since it is invalid selection
    do
    {
         height = get_int("How big you want the pyramid?\n");
    }
    while (height <= 0 || height > 8);
    
    //Check for number of rows which is the times the user says it wants as the size of the pyramid
   for (int i = 0; i < height; i++)
   {
      // BlankSpaces for loop, 
      for (int j = height - 1; j > i; j--)
      printf(" ");
      
      //Hashes # 
      for (int j = 0; j <= i; j++)
      printf("#");
      
       printf("\n");
   }
    
}