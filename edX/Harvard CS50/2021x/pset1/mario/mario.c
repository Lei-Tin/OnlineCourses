#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;

    // Repeatedly prompt the user for input unless between 1-8
    do
    {
        n = get_int("Height: ");
    }
    while (n <= 0 || n > 8);


    // Each row
    for (int i = 0; i < n; i++)
    {

        // Each column starts with spaces, n - i - 1 times
        for (int j = 0; j < n - i - 1; j++)
        {
            printf(" ");
        }

        // Followed by hashes
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }

        printf("  ");

        // Then by another hash that is the same time as i
        for (int l = 0; l < i + 1; l++)
        {
            printf("#");
        }

        printf("\n");

    }

}