//Including the libraries in able to use the code in the program
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //create an array of 100 integers where evert elemt of the array is it´s index

    //Take the array and declare it with the size of it
    int bar[100];

    //Loop for each iteration of the array we assign the value of the counter to that possition of the index of the array
    for(int j=0; j<100;j++)
    {
       bar[j] = j;
       //Printing the array
       printf("Values are: %d,\n", bar[j]);
    }
    
  

}