#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Declaring variable
    long CardNumber;


    //Repeating the question to obtain a card number
    do
    {
        CardNumber = get_long("Credit Card Number: ");
    }
    while (CardNumber <= 0);


    //Declaring all variables
    long ProcessingCard = CardNumber;
    int sum = 0;
    int digit = 0;
    long divisor;
    int FirstDigit, FirstTwoDigits, LastDigit;

    //Getting the digits of the whole card number
    while (ProcessingCard != 0)
    {
        ProcessingCard /= 10;
        digit++;
    }

    //Setting up a Processing Card Number for working
    ProcessingCard = CardNumber;

    //Getting the last digit while jumping back 2 digits at a time, and adding the numbers together
    while (ProcessingCard > 0)
    {
        LastDigit = ProcessingCard % 10;
        sum += LastDigit;
        ProcessingCard /= 100;
    }

    ProcessingCard = CardNumber / 10;

    //Getting the 2nd to the last digit, jump back 2 digits at a time, multiplying it by 2, and adding the separate numbers to the sum
    while (ProcessingCard > 0)
    {
        LastDigit = ProcessingCard % 10;
        sum += ((LastDigit * 2) % 10) + ((LastDigit * 2) / 10);
        ProcessingCard /= 100;
    }

    //Divisor setup to 10
    divisor = 10;

    //Divisor Loop to obtain the first and first two digits
    for (int i = 0; i < digit - 2; i++)
    {
        divisor *= 10;
    }


    // Setting the FirstDigit and FirstTwoDigits
    FirstDigit = CardNumber / divisor;
    FirstTwoDigits = CardNumber / (divisor / 10);


    //When the sum has a last digit of 10, starts deciding whether it's VISA, AMEX, or MASTERCARD
    //When not fulfilling any, show INVALID
    if (sum % 10 == 0)
    {

        if (FirstDigit == 4 && (digit == 13 || digit == 16))
        {
            printf("VISA\n");
        }

        else if ((FirstTwoDigits == 34 || FirstTwoDigits == 37) && digit == 15)
        {
            printf("AMEX\n");
        }

        else if ((FirstTwoDigits > 50 && FirstTwoDigits < 56) && digit == 16)
        {
            printf("MASTERCARD\n");
        }

        else
        {
            printf("INVALID\n");
        }
    }

    else
    {
        printf("INVALID\n");
    }


    // Debugging codes, showing the different variables I have

    // printf("Sum: %i\n", sum);
    // printf("Digits: %i\n", digit);
    // printf("First 2 Digits: %i\n", FirstTwoDigits);
    // printf("First Digit: %i\n", FirstDigit);
}