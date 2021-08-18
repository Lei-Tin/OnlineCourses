// Implements a dictionary's functionality

#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Word Count
int numWords;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    int key = hash(word);

    node *nodeTmp = table[key];

    while (nodeTmp != NULL)
    {
        if (strcasecmp(nodeTmp -> word, word) == 0)
        {
            return true;
        }
        nodeTmp = nodeTmp -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    int hashValue = 0;

    for (int i = 0; word[i] != '\0'; i++)
    {
        hashValue += tolower(word[i]);
    }
    return hashValue % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // TODO
    // Read dictionary input
    FILE *input = fopen(dictionary, "r");

    if (input == NULL)
    {
        return false;
    }

    char wordTmp[LENGTH + 1];


    while (fscanf(input, "%s\n", wordTmp) != EOF)
    {
        node *nodeTmp = malloc(sizeof(node));
        int key = hash(wordTmp);

        strcpy(nodeTmp -> word, wordTmp);
        if (table[key] == NULL)
        {
            table[key] = nodeTmp;
            nodeTmp -> next = NULL;
        }

        else
        {
            nodeTmp -> next = table[key];
            table[key] = nodeTmp;
        }

        numWords++;
    }

    fclose(input);

    return true;

}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return numWords;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO

    for (int i = 0; i < N; i++)
    {
        node *nodeTmp = table[i];
        while (nodeTmp != NULL)
        {
            node *connector = nodeTmp;
            nodeTmp = nodeTmp -> next;
            free(connector);
        }

        // table[i] = NULL;
        // free(table[i]);

    }

    return true;
}
