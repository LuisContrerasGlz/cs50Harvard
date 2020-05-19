//Including the libraries in able to use the code in the program
#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

/*
  Encrypted some text by shifting all of the letter of that text by a certain amount.
  
  TO DO:
  1. Get Key - the amount we will shift each of the individual letters by
  2. Get PlainText
  3. Encipher
  4. Print ciphertext
*/

//Declaring a valid_key function
bool valid_key(string s);

int main(int argc, string argv[])
{
    //Check for a valid key fron the user
    if (argc != 2 || !valid_key(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
        
    }
    //extract the key converting from the char ASCII to int
    int key = atoi(argv[1]);
    
    //Take the plaintext from the user
    string plaintext = get_string("plaintext: ");
    
    //Print the ciphertext
    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        char c = plaintext[i];
        if (isalpha(c))
        {
            char m = 'A';
            if(islower(c))
                m = 'a';
                printf("%c", (c - m + key) % 26 + m);
        }
        else 
            printf("%c", c);
    }
    printf("\n");
}

//Valid key funtion definition
bool valid_key(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
        if (!isdigit(s[i]))
         return false;
    return true;
}