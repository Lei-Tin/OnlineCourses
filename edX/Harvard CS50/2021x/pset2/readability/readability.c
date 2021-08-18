#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int findIndex(int letter, int word, int sentence);

int main(void)
{

    string input = NULL;

    while (input == NULL)
    {
        input = get_string("Text: ");
    }

    int letter = 0;

    // I counted every space as a word, so I should add one word in the end.
    // For example, I will use | as a word counter
    // I| like| to| eat| pineapples, I don't have a counter after pineapple, so I will add one myself
    int word = 1;
    int sentence = 0;

    int var = 0;

    for (int i = 0; i < strlen(input); i++)
    {
        if (isalpha(input[i]) != 0)
        {
            letter++;
        }

        if (isspace(input[i]) != 0)
        {
            word++;
        }

        if (input[i] == '!' || input[i] == '?' || input[i] == '.')
        {
            sentence++;
        }
    }

    int index = findIndex(letter, word, sentence);

    if (index >= 16)
    {
        printf("Grade 16+\n");
        return 0;
    }

    if (index < 1)
    {
        printf("Before Grade 1\n");
        return 0;
    }

    printf("Grade %i\n", index);
    return 0;

    // Debug testing code
    // printf("Letters: %i\n", letter);
    // printf("Words: %i\n", word);
    // printf("Sentences: %i\n", sentence);

}

int findIndex(int letter, int word, int sentence)
{
    // Forgot
    float L = ((float)letter / (float)word) * 100;
    float S = ((float)sentence / (float)word) * 100;

    return (round((0.0588 * L) - (0.296 * S) - 15.8));
}