#include "helpers.h"
#include <math.h>
#include <cs50.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            int average = round((image[row][column].rgbtRed + image[row][column].rgbtGreen + image[row][column].rgbtBlue) / (float) 3);
            image[row][column].rgbtRed = average;
            image[row][column].rgbtGreen = average;
            image[row][column].rgbtBlue = average;
        }
    }


    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //Creating a tempColors for the copy of image
    RGBTRIPLE tempColors[height][width];

    //Copying the image to tempColors
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            tempColors[row][column] = image[row][column];
        }
    }

    //Actually printing the reveresed image in horizontal
    for (int row = 0; row <= height; row++)
    {
        for (int column = width - 1, j = 0; column >= 0; column--, j++)
        {
            image[row][j] = tempColors[row][column];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tempColors[height][width];

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            tempColors[row][column] = image[row][column];
        }
    }

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            if (row == 0 && column == 0)  // top left corner case (corners 1:4)
            {
                int blurredR = round((tempColors[row][column].rgbtRed + tempColors[row][column + 1].rgbtRed + tempColors[row + 1][column].rgbtRed + tempColors[row + 1][column + 1].rgbtRed) / (float) 4);
                int blurredB = round((tempColors[row][column].rgbtBlue + tempColors[row][column + 1].rgbtBlue + tempColors[row + 1][column].rgbtBlue + tempColors[row + 1][column + 1].rgbtBlue) / (float) 4);
                int blurredG = round((tempColors[row][column].rgbtGreen + tempColors[row][column + 1].rgbtGreen + tempColors[row + 1][column].rgbtGreen + tempColors[row + 1][column + 1].rgbtGreen) / (float) 4);

                image[row][column].rgbtRed = blurredR;
                image[row][column].rgbtBlue = blurredB;
                image[row][column].rgbtGreen = blurredG;
                continue;
            }

            if (row == 0 && column == width - 1)  // top right corner case (corners 2:4)
            {
                int blurredR = round((tempColors[row][column].rgbtRed + tempColors[row][column - 1].rgbtRed + tempColors[row + 1][column].rgbtRed + tempColors[row + 1][column - 1].rgbtRed) / (float) 4);
                int blurredB = round((tempColors[row][column].rgbtBlue + tempColors[row][column - 1].rgbtBlue + tempColors[row + 1][column].rgbtBlue + tempColors[row + 1][column - 1].rgbtBlue) / (float) 4);
                int blurredG = round((tempColors[row][column].rgbtGreen + tempColors[row][column - 1].rgbtGreen + tempColors[row + 1][column].rgbtGreen + tempColors[row + 1][column - 1].rgbtGreen) / (float) 4);

                image[row][column].rgbtRed = blurredR;
                image[row][column].rgbtBlue = blurredB;
                image[row][column].rgbtGreen = blurredG;
                continue;
            }

            if (row == height - 1 && column == 0)  // bottom left corner case  (corners 3:4)
            {
                int blurredR = round((tempColors[row][column].rgbtRed + tempColors[row][column + 1].rgbtRed + tempColors[row - 1][column].rgbtRed + tempColors[row - 1][column + 1].rgbtRed) / (float) 4);
                int blurredB = round((tempColors[row][column].rgbtBlue + tempColors[row][column + 1].rgbtBlue + tempColors[row - 1][column].rgbtBlue + tempColors[row - 1][column + 1].rgbtBlue) / (float) 4);
                int blurredG = round((tempColors[row][column].rgbtGreen + tempColors[row][column + 1].rgbtGreen + tempColors[row - 1][column].rgbtGreen + tempColors[row - 1][column + 1].rgbtGreen) / (float) 4);

                image[row][column].rgbtRed = blurredR;
                image[row][column].rgbtBlue = blurredB;
                image[row][column].rgbtGreen = blurredG;
                continue;
            }

            if (row == height - 1 && column == width - 1)  // bottom right corner case  (corners 4:4)
            {
                int blurredR = round((tempColors[row][column].rgbtRed + tempColors[row][column - 1].rgbtRed + tempColors[row - 1][column].rgbtRed + tempColors[row - 1][column - 1].rgbtRed) / (float) 4);
                int blurredB = round((tempColors[row][column].rgbtBlue + tempColors[row][column - 1].rgbtBlue + tempColors[row - 1][column].rgbtBlue + tempColors[row - 1][column - 1].rgbtBlue) / (float) 4);
                int blurredG = round((tempColors[row][column].rgbtGreen + tempColors[row][column - 1].rgbtGreen + tempColors[row - 1][column].rgbtGreen + tempColors[row - 1][column - 1].rgbtGreen) / (float) 4);

                image[row][column].rgbtRed = blurredR;
                image[row][column].rgbtBlue = blurredB;
                image[row][column].rgbtGreen = blurredG;
                continue;
            }

            if (row == 0)  // top row case  (rows 1: 4)
            {
                if (column != 0 && column != width - 1)  //  top row but not corners case
                {
                    int blurredR = round((tempColors[row][column - 1].rgbtRed + tempColors[row][column].rgbtRed + tempColors[row][column + 1].rgbtRed + tempColors[row + 1][column - 1].rgbtRed + tempColors[row + 1][column].rgbtRed + tempColors[row + 1][column + 1].rgbtRed) / (float) 6);
                    int blurredG = round((tempColors[row][column - 1].rgbtGreen + tempColors[row][column].rgbtGreen + tempColors[row][column + 1].rgbtGreen + tempColors[row + 1][column - 1].rgbtGreen + tempColors[row + 1][column].rgbtGreen + tempColors[row + 1][column + 1].rgbtGreen) / (float) 6);
                    int blurredB = round((tempColors[row][column - 1].rgbtBlue + tempColors[row][column].rgbtBlue + tempColors[row][column + 1].rgbtBlue + tempColors[row + 1][column - 1].rgbtBlue + tempColors[row + 1][column].rgbtBlue + tempColors[row + 1][column + 1].rgbtBlue) / (float) 6);

                    image[row][column].rgbtRed = blurredR;
                    image[row][column].rgbtBlue = blurredB;
                    image[row][column].rgbtGreen = blurredG;
                    continue;
                }
            }

            if (column == 0)  // left column case (rows 2: 4)
            {
                if (row != 0 && row != height - 1)  //  left column but not corner case
                {
                    int blurredR = round((tempColors[row - 1][column].rgbtRed + tempColors[row - 1][column + 1].rgbtRed + tempColors[row][column].rgbtRed + tempColors[row][column + 1].rgbtRed + tempColors[row + 1][column].rgbtRed + tempColors[row + 1][column + 1].rgbtRed) / (float) 6);
                    int blurredG = round((tempColors[row - 1][column].rgbtGreen + tempColors[row - 1][column + 1].rgbtGreen + tempColors[row][column].rgbtGreen + tempColors[row][column + 1].rgbtGreen + tempColors[row + 1][column].rgbtGreen + tempColors[row + 1][column + 1].rgbtGreen) / (float) 6);
                    int blurredB = round((tempColors[row - 1][column].rgbtBlue + tempColors[row - 1][column + 1].rgbtBlue + tempColors[row][column].rgbtBlue + tempColors[row][column + 1].rgbtBlue + tempColors[row + 1][column].rgbtBlue + tempColors[row + 1][column + 1].rgbtBlue) / (float) 6);

                    image[row][column].rgbtRed = blurredR;
                    image[row][column].rgbtBlue = blurredB;
                    image[row][column].rgbtGreen = blurredG;
                    continue;
                }
            }

            if (column == width - 1)  // right column case (rows 3: 4)
            {
                if (row != 0 && row != height - 1)  //  right column but not corner case
                {
                    int blurredR = round((tempColors[row - 1][column - 1].rgbtRed + tempColors[row - 1][column].rgbtRed + tempColors[row][column - 1].rgbtRed + tempColors[row][column].rgbtRed + tempColors[row + 1][column - 1].rgbtRed + tempColors[row + 1][column].rgbtRed) / (float) 6);
                    int blurredG = round((tempColors[row - 1][column - 1].rgbtGreen + tempColors[row - 1][column].rgbtGreen + tempColors[row][column - 1].rgbtGreen + tempColors[row][column].rgbtGreen + tempColors[row + 1][column - 1].rgbtGreen + tempColors[row + 1][column].rgbtGreen) / (float) 6);
                    int blurredB = round((tempColors[row - 1][column - 1].rgbtBlue + tempColors[row - 1][column].rgbtBlue + tempColors[row][column - 1].rgbtBlue + tempColors[row][column].rgbtBlue + tempColors[row + 1][column - 1].rgbtBlue + tempColors[row + 1][column].rgbtBlue) / (float) 6);

                    image[row][column].rgbtRed = blurredR;
                    image[row][column].rgbtBlue = blurredB;
                    image[row][column].rgbtGreen = blurredG;
                    continue;
                }
            }

            if (row == height - 1)  // bottom row case  (rows 4: 4)
            {
                if (column != 0 && column != width - 1)  //  botom row but not corners case
                {
                    int blurredR = round((tempColors[row - 1][column - 1].rgbtRed + tempColors[row - 1][column].rgbtRed + tempColors[row - 1][column + 1].rgbtRed + tempColors[row][column - 1].rgbtRed + tempColors[row][column].rgbtRed + tempColors[row][column + 1].rgbtRed) / (float) 6);
                    int blurredG = round((tempColors[row - 1][column - 1].rgbtGreen + tempColors[row - 1][column].rgbtGreen + tempColors[row - 1][column + 1].rgbtGreen + tempColors[row][column - 1].rgbtGreen + tempColors[row][column].rgbtGreen + tempColors[row][column + 1].rgbtGreen) / (float) 6);
                    int blurredB = round((tempColors[row - 1][column - 1].rgbtBlue + tempColors[row - 1][column].rgbtBlue + tempColors[row - 1][column + 1].rgbtBlue + tempColors[row][column - 1].rgbtBlue + tempColors[row][column].rgbtBlue + tempColors[row][column + 1].rgbtBlue) / (float) 6);

                    image[row][column].rgbtRed = blurredR;
                    image[row][column].rgbtBlue = blurredB;
                    image[row][column].rgbtGreen = blurredG;
                    continue;
                }
            }
            // center case
            int blurredR = round((tempColors[row - 1][column - 1].rgbtRed + tempColors[row - 1][column].rgbtRed + tempColors[row - 1][column + 1].rgbtRed + tempColors[row][column - 1].rgbtRed + tempColors[row][column].rgbtRed + tempColors[row][column + 1].rgbtRed+ tempColors[row + 1][column - 1].rgbtRed + tempColors[row + 1][column].rgbtRed + tempColors[row + 1][column + 1].rgbtRed) / (float) 9);
            int blurredG = round((tempColors[row - 1][column - 1].rgbtGreen + tempColors[row - 1][column].rgbtGreen + tempColors[row - 1][column + 1].rgbtGreen + tempColors[row][column - 1].rgbtGreen + tempColors[row][column].rgbtGreen + tempColors[row][column + 1].rgbtGreen + tempColors[row + 1][column - 1].rgbtGreen + tempColors[row + 1][column].rgbtGreen + tempColors[row + 1][column + 1].rgbtGreen) / (float) 9);
            int blurredB = round((tempColors[row - 1][column - 1].rgbtBlue + tempColors[row - 1][column].rgbtBlue + tempColors[row - 1][column + 1].rgbtBlue + tempColors[row][column - 1].rgbtBlue + tempColors[row][column].rgbtBlue + tempColors[row][column + 1].rgbtBlue + tempColors[row + 1][column - 1].rgbtBlue + tempColors[row + 1][column].rgbtBlue + tempColors[row + 1][column + 1].rgbtBlue) / (float) 9);

            image[row][column].rgbtRed = blurredR;
            image[row][column].rgbtBlue = blurredB;
            image[row][column].rgbtGreen = blurredG;

        }
    }

    return;
}

int max(int input)
{
    //Trying out the tertiary operator? Sounds cool
    return (input < 255 ? input : 255);
}

RGBTRIPLE edged_pixel(int i, int j, int height, int width, RGBTRIPLE image[height][width])
{
    //Initializing variables
    int redX, greenX, blueX, redY, greenY, blueY;
    redX = greenX = blueX = redY = greenY = blueY = 0;

    //2d array of Gx
    int Gx[3][3] = {{-1, 0, 1} , {-2, 0, 2} , {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    //Iterate through -1, 0, +1 vertically. di = displaced i
    for (int di = -1; di <= 1; di++)
    {
        //Iterate through -1, 0, +1 horizontally. dj = displaced j
        for (int dj = -1; dj <= 1; dj++)
        {
            if (i + di >= 0 && i + di < height && j + dj >= 0 && j + dj < width)
            {
                //Iterate through all 3 values, cuz the first value start with -1
                int multiplierX = Gx[di + 1][dj + 1];
                redX += multiplierX * image[i + di][j + dj].rgbtRed;
                greenX += multiplierX * image[i + di][i + dj].rgbtGreen;
                blueX += multiplierX * image[i + di][i + dj].rgbtBlue;

                int multiplierY = Gy[di + 1][dj + 1];
                redY += multiplierY * image[i + di][j + dj].rgbtRed;
                greenY += multiplierY * image[i + di][i + dj].rgbtGreen;
                blueY += multiplierY * image[i + di][i + dj].rgbtBlue;
            }
        }
    }

    //Using the formula given in the pset website and giving it to returnPixel, which will be returned as a result in the edged_pixel function
    RGBTRIPLE pixel;
    pixel.rgbtRed = max(round(sqrt(redX*redX + redY*redY)));
    pixel.rgbtGreen = max(round(sqrt(greenX*greenX + greenY*greenY)));
    pixel.rgbtBlue = max(round(sqrt(blueX*blueX + blueY*blueY)));

    return pixel;

}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tempImage[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            //Running the function of "edged_pixel"
            tempImage[row][column] = edged_pixel(row, column, height, width, image);
        }
    }

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            image[row][column] = tempImage[row][column];
        }
    }
    return;
}
