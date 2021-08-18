//Including Dependencies
#include <stdio.h>
#include <cs50.h>

//Framework
int main(void)
{
    //Changed it to Hello (name)! Good World!
    //Having the return character in the end of every line
    //Included the get_string function in the reference of %s in the answer
    printf("Hello %s! Good World!\n", get_string("What is your name?\n"));
    
}