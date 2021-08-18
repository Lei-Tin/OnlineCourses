#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Instantly quit the application if it's not 2 command line arguments
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // If key is not 26 in length, quit
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Initializing key as argv[1]
    string key = argv[1];

    int repeats = 0;

    for (int i = 0; i < 26; i++)
    {
        if (isalpha(key[i]) == 0)
        {
            printf("Invalid key.\n");
            return 1;
        }

        // Calculating for repeats within the key
        repeats = 0;

        for (int j = 0; j < 26; j++)
        {
            if (key[i] == key[j])
            {
                repeats++;
            }
        }

        if (repeats == 2)
        {
            printf("Key contains repeated characters!\n");
            return 1;
        }

    }

    // Repeat for every single letter in the first command-line argument and assign it to key[i]
    for (int i = 0; i < 26; i++)
    {
        key[i] = toupper(argv[1][i]);
    }

    string plain = get_string("plaintext:  ");

    char cipher[strlen(plain)];


    // Repeat like 26 times per letter to replace
    for (int i = 0; i < strlen(plain); i++)
    {
        // Copy cipher[i] to key[i] to solve punctuations and numbers
        cipher[i] = plain[i];

        // Lower letter case
        for (int j = 65; j <= 90; j++)
        {
            if ((int)plain[i] == j)
            {
                cipher[i] = toupper(key[j - 65]);
            }
        }


        // Capital letter case
        for (int k = 97; k <= 122; k++)
        {
            if ((int)plain[i] == k)
            {
                cipher[i] = tolower(key[k - 97]);
            }
        }

    }


    // Final output
    printf("ciphertext: ");

    for (int i = 0; i < strlen(plain); i++)
    {
        printf("%c", cipher[i]);
    }

    printf("\n");

}