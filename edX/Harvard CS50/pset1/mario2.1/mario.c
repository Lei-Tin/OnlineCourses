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


        for (c = 0; c < r + 1; c++)
        {
            printf("#");
        }

        printf("  ");

        for (c = 0; c < r + 1; c++)
        {
            printf("#");
        }

        printf("\n");

    }

}



/*
Now this feels like google docs
Sponsors; spain, uk, rwanda
signatories: rest of the world
topic: Using cs50 ide to hack the world government nuclear codes
committee: CS50
*/