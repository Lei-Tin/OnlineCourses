#include <stdio.h>
#include <cs50.h>

int dotsInTriangle(int n);

int main(void)
{

    int layers = get_int("Layers: ");

    // printf("Dots: %i\n", dotsInTriangle(get_int("Layers: ")));

    // Per row
    for (int i = 0; i < layers; i++)
    {
        for (int j = layers; j > i + 1; j--)
        {
            printf(" ");
        }

        for (int k = 0; k < i + 1; k++)
        {
            printf("**");
        }

        for (int j = layers; j > i + 1; j--)
        {
            printf(" ");
        }

        printf("    ");

        printf("Cumulative dots: %i\n", dotsInTriangle(i + 1) * 2);

    }

}

int sum = 0;

int dotsInTriangle(int n)
{

    // Algorithm 1 - For loop, mathematical

    for (int i = 1; i <= n; i++)
    {
        sum += i;
    }

    return sum;

    // Algorithm 2 - Recusrive

    if (n == 1)
    {
        return 1;
    }
    else
    {
        return n + dotsInTriangle(n - 1);
    }

}

