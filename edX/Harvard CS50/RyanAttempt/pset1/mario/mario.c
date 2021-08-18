#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    do
    {

        height = get_int("ENTER THE HEIGHT HERE: ");

    }
    while (height <= 0 || height >= 9);

    for (int i = 0; i < height; i++)
    {

        for (int j = 0; j < height - (i + 1); j++)
        {
            printf(" ");
        }

        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }

        for (int l = 0; l < 2; l++)
        {
            printf(" ");
        }

        for (int m = 0; m <= i; m++)
        {
            printf("#");
        }

        printf("\n");
    }

}