#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{

    // Initializing Variables
    int digits = 0;
    long inputCard, cardTmp;

    // Using a forever loop
    while (true)
    {
        digits = 0;

        inputCard = get_long("Number: ");

        cardTmp = inputCard;

        do
        {
            cardTmp /= 10;
            digits++;
        }
        while (cardTmp > 0);

        if (digits != 13 && digits != 15 && digits != 16)
        {
            // If the input is not what we wanted, output invalid right away
            printf("INVALID\n");
            return 0;
        }

        // If the user entered a normal card, break out of the loop
        if (digits == 13 || digits == 15 || digits == 16)
        {
            break;
        }

    }

    cardTmp = inputCard / 10;

    int checkSum = 0;
    int n;

    do
    {

        // n being the odd number in the card number
        n = (cardTmp % 10) * 2;

        if (n >= 10)
        {
            n = n % 10;
            n += 1;
        }

        checkSum += n;

        cardTmp /= 100;

    }
    while (cardTmp > 0);

    cardTmp = inputCard;

    do
    {

        n = cardTmp % 10;

        checkSum += n;

        cardTmp /= 100;

    }
    while (cardTmp > 0);


    // Debug line
    // printf("Digits: %i\n", digits);

    // Using pow as exponents to obtain the first 2 digits of the card
    int firstTwoDigits = inputCard / pow(10, digits - 2);

    int firstDigit = firstTwoDigits / 10;

    if (checkSum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // Using an array to store the types of card that I have
    string cardType[3] = {"AMEX", "MASTERCARD", "VISA"};


    // Starts with 34 and 37, total 15 digits
    if (digits == 15 && (firstTwoDigits == 34 || firstTwoDigits == 37))
    {
        printf("%s\n", cardType[0]);
    }

    // Starts with 51, 52, 53, 54, 55, total 16 digits
    else if (digits == 16 && (firstTwoDigits > 50 && firstTwoDigits < 56))
    {
        printf("%s\n", cardType[1]);
    }

    // Starts with 4, total 13 digits
    else if ((digits == 13 || digits == 16) && firstDigit == 4)
    {
        printf("%s\n", cardType[2]);
    }

    else
    {
        printf("INVALID\n");
    }



    // Debug line
    // printf("first2: %i\nfirst: %i\n", firstTwoDigits, firstDigit);


    // Debug line
    // printf("checkSum: %i\n", checkSum);

}