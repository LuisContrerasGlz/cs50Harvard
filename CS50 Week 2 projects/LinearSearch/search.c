#include <cs50.h>
#include <stdio.h>

/*
    Here we initialize an array with some values, and we check the items in the array one at a time, in order.
    And in each case, depending on whether the value was found or not, we can return an exit code of either 0 (for success) or 1 (for failure).
*/
int main(void)
{
    // An array of numbers
    int numbers[] = {4, 8, 15, 16, 23, 42};

    // Search for 50
    for (int i = 0; i < 6; i++)
    {
        if (numbers[i] == 50)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}