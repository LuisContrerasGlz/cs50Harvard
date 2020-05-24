#include <cs50.h>
#include <stdio.h>
#include <string.h>

//we create our own type with a struct called person, which will have a string called name and a string called number
typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    //we can create an array of these struct types and initialize the values inside each of them, using a new syntax, ., to access the properties of each person.
    person people[4];

    people[0].name = "EMMA";
    people[0].number = "617–555–0100";

    people[1].name = "RODRIGO";
    people[1].number = "617–555–0101";

    people[2].name = "BRIAN";
    people[2].number = "617–555–0102";

    people[3].name = "DAVID";
    people[3].number = "617–555–0103";

    // Search for EMMA
    //In our loop, we can now be more certain that the number corresponds to the name since they are from the same person element.
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(people[i].name, "EMMA") == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}