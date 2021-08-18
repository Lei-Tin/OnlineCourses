#include <cs50.h>
#include <stdio.h>

int main(void)
{

    // Initialize starting size

    int sizeTmp = 0;

    // While it is not greater than 9, continue prompting the user
    while (sizeTmp < 9)
    {
        sizeTmp = get_int("Start size: ");
    }

    // Initialize the starting value

    int endingSize = 0;

    while (endingSize < sizeTmp)
    {
        endingSize = get_int("Ending size: ");
    }



    // Initialize the variables

    int years = 0;

    int currSize = sizeTmp;

    // While current size in this year is lesser than the targetted amount, then run the loop again
    while (currSize < endingSize)
    {
        sizeTmp = currSize;

        years++;

        currSize += sizeTmp / 3;
        currSize -= sizeTmp / 4;

        // Debug codes
        // printf("currSize: %i\n", currSize);
        // printf("sizeTmp: %i\n", sizeTmp);
    }

    // Output
    printf("Years: %i\n", years);

}