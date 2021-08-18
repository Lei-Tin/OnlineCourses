#include <cs50.h>
#include <stdio.h>

int recursive(int n);

int increment=1;
int sum = 0;

int main(void)
{
    int n = get_int("Layer: "); //n th layer

    recursive(n);

    printf("Dots: %i\n", sum);
}

int recursive(int n)
{
    sum += increment;

    if (n < 1)
    {
        return sum = 0;
    }

    if (n == 1)
    {
        return sum;
    }

    increment++;

    return recursive(n-1);
}
