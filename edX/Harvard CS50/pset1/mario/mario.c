#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Getting h as height
    int h;

    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);

    //Declaring r for Row, c for Column, and b for Blanks
    int r;
    int c;
    int b;

    //Every single row works with this
    for (r = 0; r < h; r++)
    {
        //Printing in the spaces before the actual pyramid
        for (b = 0; b < h - r - 1; b++)
        {
            printf(" ");
        }

        //Printing in the hash, because of the spaces, it is right aligned
        for (c = 0; c <= r; c++)
        {
            printf("#");
        }

        //The isolated fixed 2 distance of the pyramid
        printf("  ");

        //Copy pasted the code on top since if we have no space before, it will be left aligned.
        for (c = 0; c <= r; c++)
        {
            printf("#");
        }

        //The ending change row
        printf("\n");
    }
}