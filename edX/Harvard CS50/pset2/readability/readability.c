#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//Declaring function at the start
float index(float L, float S);

int main(void)
{
    //Declaring variables, inputs, etc.
    string input;

    //Prompting input
    input = get_string("Please input the thing here: ");

    //Getting the string length
    int length = strlen(input);

    //Declaring essential variables
    int letters = 0;
    int words = 0;
    int sentences = 0;


    //Using arrays to obtain individual chars of the string input
    for (int i = 0; i < length; i++)
    {
        if (isalpha(input[i]))
        {
            letters++;
        }
        else if (input[i] == '!' || input[i] == '.' || input[i] == '?')
        {
            sentences++;
        }
        else if (input[i] == ' ')
        {
            words++;
        }

    }

    //Counting spaces for words require 1 more space in the end
    words++;

    //Calculating the grade that is needed
    int level = round(index((letters / (float) words) * 100, (sentences / (float) words) * 100));

    //Debugging used codes
    // printf("Letters: %i\n", letters);
    // printf("Words: %i\n", words);
    // printf("Sentences: %i\n", sentences);
    // printf("Index: %i\n", level);

    //Final printing in the answers
    if (level < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (level > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", level);
    }

}

//The function for index
float index(float L, float S)
{
    float answer = (0.0588 * L) - (0.296 * S) - 15.8;
    return answer;
}