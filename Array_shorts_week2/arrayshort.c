//Including the libraries in able to use the code in the program
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Copy the content of 1 array into another array:

    //Take the 2 arrays and define its values
    int foo[5] = {1,2,3,4,5};
    int bar[5];

    //Loop for each value of the array and passing its values to the other one, each iteration you assign the value to the index of the counter
    for(int j=0; j<5;j++)
    {
       bar[j] = foo[j];
       //Printing the array foo
       printf("Foo Values are: %d,\n", foo[j]);
    }
    
    //check how to print the content of an array in C.
    printf("Now bar has the same values as foo which are: %d,%d,%d,%d,%d,\n",bar[0],bar[1],bar[2],bar[3],bar[4]);
    
    

}