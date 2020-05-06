//Including the libraries in able to use the code in the program
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //prompt the user for their name
    string name = get_string("What is your name?\n");
    //formatint the string for print the result to the User
    printf("hello, %s\n", name);
}