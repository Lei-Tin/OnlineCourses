#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner


    // Print results
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }

    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }

    else
    {
        printf("Tie!\n");
    }

}



int compute_score(string word)
{
    // TODO: Compute and return score for string

    // Big brain formula
    int sum = 0;

    // strlen imported from string.h
    for (int i = 0; i < strlen(word); i++)
    {
        for (int j = 65; j <= 90; j++)
        {

            // Convert to upper case of each letter, compare to 65 and 90 according to ASCII chart
            // toupper imported from ctype.h
            if ((int)toupper(word[i]) == j)
            {
                // Locating array back to 0 - 25 index
                sum += POINTS[j - 65];
            }
        }
    }


    // Return answer
    return sum;

}
