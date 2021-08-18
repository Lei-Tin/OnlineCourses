#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

/*
PSEUDOCODE

Open memory card
Repeat until end of card (do while loop or while true loop + break)
    Read 512 bytes into buffer


    If start of new jpeg (0xff 0xd8 0xff and 0xe0 all the way to 0xef)
        If first jpeg
            fwrite data
            found jpeg = 1
            write 001

        else
            fwrite data jpeg 002 continue
            found jpeg = 1
            write 002 or loop plus plus plus

    else if already found jpeg (found jpeg = 1)
        fwrite data continue

Close remaining files


*/

int main(int argc, char *argv[])
{
    //Block size is 512
    int BLOCK_SIZE = 512;
    int current_fileNum = 0;
    bool first_jpeg = false;
    bool found_jpeg = false;
    char current_fileName[100];

    //Type def BYTE
    typedef uint8_t BYTE;

    BYTE buffer[BLOCK_SIZE];
    size_t bytes;

    //If user doesn't enter ./recover xxx
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    //Open the file, but if file doesn't exist or failed to open, say we failed to open your file
    FILE *file = fopen(argv[1], "r");
    FILE *current_file;

    if (file == NULL)
    {
        printf("Failed to open: %s\n", argv[1]);
        return 1;
    }

    do
    {
        bytes = fread(buffer, sizeof(BYTE), BLOCK_SIZE, file);

        //Is start of JPEG file?
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //Found jpeg
            found_jpeg = true;

            //If not first jpeg, make it first jpeg
            if (first_jpeg == false)
            {
                first_jpeg = true;
            }

            else
            {
                //Close the current file
                fclose(current_file);
            }
            //Change current_fileName to 000.jpg
            sprintf(current_fileName, "%03i.jpg", current_fileNum);

            //Set current_file, a file type to open 000.jpg, and get it to write
            current_file = fopen(current_fileName, "w");

            //Actually writing in the stuffs from buffer into current_file
            fwrite(buffer, sizeof(BYTE), bytes, current_file);

            //Increase the current_file indicator to actually name the files
            current_fileNum++;
        }
        else
        {
            //If JPEG is found, then continue writing the thing for 1 byte.
            if (found_jpeg == true)
            {
                fwrite(buffer, sizeof(BYTE), bytes, current_file);
            }
        }
    }
    //Do while loop, where when bytes read is 0, signalizing end of file
    while (bytes != 0);

    //Close whatever file still open
    fclose(file);
    fclose(current_file);

    return 0;
}
