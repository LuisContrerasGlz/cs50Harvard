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
    
    //Check for number of rows
   for (int i = 0; i < height; i++)
   {
       //Check for number of times it needs to print the # and space
       for (int j = 0; j < height; j++)
       {
           if(i+j < height -1 )
           printf(" ");   
           else printf("#"); 
       }
        printf("\n");
       
   }
    
}