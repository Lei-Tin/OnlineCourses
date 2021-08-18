#include <stdio.h>
#include <cs50.h>
#include <math.h>
//Including math.h for round()

int main(void)
{
    float dollars_input;
    do
    {
        dollars_input = get_float("Change owed: ");
    }
    while (dollars_input <= 0);

    //Using round to make sure that the number doesn't have decimals
    int cents = round(dollars_input * 100);
    int coins_needed = 0;

    //If we have greater than 25, then we cut by 25 and check again
    while (cents >= 25)
    {
        cents = cents - 25;
        coins_needed = coins_needed + 1;
    }
    //If we have more than 10, then go again and cut by 10
    while (cents >= 10)
    {
        cents = cents - 10;
        coins_needed = coins_needed + 1;
    }
    //Same as above, but 5
    while (cents >= 5)
    {
        cents = cents - 5;
        coins_needed = coins_needed + 1;
    }
    //Same as above but 1
    while (cents >= 1)
    {
        cents = cents - 1;
        coins_needed = coins_needed + 1;
    }
    //Print out the result in the end
    printf("Coins Needed: %i\n", coins_needed);
}