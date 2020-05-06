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
    
    //loop that will create the number of rows in the pyramid entered by the user
    for (int rows = 1; rows <= height; rows++) 
    {
        for (space = (height - rows); space > 0; space--)
        {
            printf(" "); 
        }
 
        for (int j = 1; j <= rows; j++)
        {   
            printf("#"); 
        }
 
        printf("\n");
    }
    
}