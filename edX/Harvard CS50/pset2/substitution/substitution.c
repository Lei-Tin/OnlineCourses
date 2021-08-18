#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

bool key_check(string key_input);

int main(int argc, string argv[])
{
    if (argc == 2)
    {

        // Check if there are second terms involved
        if (key_check(argv[1]) == true)

        {
            // Obtaining the string that the user wants to encrypt
            string input = get_string("plaintext: ");
            string difference = argv[1];

            // For every A - Z character, set the difference of that character to itself capital
            for (int i = 'A'; i <= 'Z'; i++)

            {
                difference[i - 'A'] = toupper(difference[i - 'A']) - i;
            }


            printf("ciphertext: ");

            // For every letter input, add it to difference of the letter, and subtract it by itself, the original one
            for (int i = 0, len = strlen(input); i < len; i++)
            {
                if (isalpha(input[i]) != 0)
                {
                    input[i] = input[i] + difference[input[i] - (isupper(input[i]) ? 'A' : 'a')];
                }
                printf("%c", input[i]);
            }
            printf("\n");
        }

        // Reject the input
        else if (key_check(argv[1]) == false)

        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }

    }
    else
        // Rejecting another input
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

}

// The function for checking if a key is valid
bool key_check(string key_input)
{
    int l = strlen(key_input);
    if (l != 26)
    {
        return false;
    }

    int frequency[26] = {0};
    for (int i = 0; i < l; i++)
    {
        if (isalpha(key_input[i]) == 0)
        {
            return false;
        }

        int index = toupper(key_input[i]) - 'A';
        if (frequency[index] > 0)
        {
            return false;
        }
        frequency[index]++;
    }

    return true;

}