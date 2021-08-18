#include <cs50.h>
#include <stdio.h>
#include <unistd.h>

int main(void)
{
    long i = 1;
    while(true)
    {
        printf ("%ld\n", i);
        i *= 2;
        sleep(1);
    }
}

// stop it, get some help
// rip aws.amazon.com, cs50 ide, and virtual machine having to get fucked by overflow