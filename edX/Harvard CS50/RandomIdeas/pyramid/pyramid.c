/*

*
**
***
****

Layers of pyramid = n

get input n for layers

use recursive function to return value of dots in pyramid, cumulative

example:

when n = 1
dots = 1

when n = 2
dots = 3

when n = 3
dots = 6

when n = 4
dots = 10

*/

#include <stdio.h>
#include <cs50.h>

int dotsInTriangle(int n);

int main(void)
{
    int input = get_int("Layers: ");

    printf("Dots: %i\n", dotsInTriangle(input));
}

int dotsInTriangle(int n)
{

    // TODO

    if (n == 1)
    {
        return 1;
    }

    else
    {
        return n + dotsInTriangle(n - 1);
    }

    // 1
    // 1 + 2
    // 1 + 2 + 3

    // return ((n * (n + 1) / 2));

}