#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Declare integers
    int h, r, c, b;

    //The loop that forces the user to give a number between 1 and 8
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);

    //Row loop, outer most
    for (r = 0; r < h; r++)
    {

        //Blank loop
        for (b = 0; b < h - r - 1; b++)
        {
            printf(" ");
        }

        //Hash loops
        for (c = 0; c <= r; c++)
        {
            printf("#");
        }

        printf("\n");

    }

}