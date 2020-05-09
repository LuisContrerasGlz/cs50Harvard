//Including the libraries in able to use the code in the program
#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

//Program to that takes as input some text and outputs the US level that is appropiate for that text

int main(void)
{
    //Getting the String that User will be providing    
    string s = get_string("Text: ");
   
    //Declaring the variables for the numer of words, sentences and letters
    int num_words, num_sentences, num_letters;
    //Setting the start values to 0
    num_words = num_sentences = num_letters = 0;
    //looping over the string
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        //Check if there is a letter and incrementing the number of letters in the program
        if (isalpha(s[i]))
        {
            num_letters++;
        }
        if ((i == 0 && s[i] != ' ') 
            || (i != len - 1 && s[i] == ' ' && s[i + 1] != ' '))
        {
            num_words++;
        }
        if (s[i] == '.' || s[i] == '?' || s[i] == '!')
        {
            num_sentences++;
        }
    }
   
    //Calculating L and S
    float L = (num_letters / (float) num_words) * 100;
    float S = (num_sentences / (float) num_words) * 100;
   
    //plug them into the Coleman-Liau Index formula.
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    
    //Calculating the grade of the text
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }   
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else 
    {
        printf("Grade %i\n", index);
    }
}
