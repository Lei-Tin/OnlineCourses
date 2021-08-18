#include <stdio.h>
#include <unistd.h>
#include <cs50.h>

//Now we gotta try for the short
//This is people intercepting in ur code

int main()
{
    for (short i = 7; true; i *= 2)
    {
        printf("%hi\n", i);
        sleep(1);
    }
}


//E F F I C I E N C Y   T O   T H E   M A X
// efficiency is true laziness -- Echo
// I dont even know if u compiled it already
// This explodes at like 5 digits