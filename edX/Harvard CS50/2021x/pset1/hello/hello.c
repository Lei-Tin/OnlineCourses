#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Print in "Hello ???" where ??? is the input that the user types
    printf("Hello %s\n", get_string("What is your name?\n"));
}