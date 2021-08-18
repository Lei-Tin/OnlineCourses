from cs50 import get_int


while True:
    CardNumber = get_int("Credit Card Number: ")
    if CardNumber >= 0:
        break

ProcessingCard = CardNumber
Sum = 0
digit = 0
FirstDigit = 0
FirstTwoDigits = 0
LastDigit = 0

while True:
    if int(ProcessingCard) == 0:
        break

    ProcessingCard /= 10
    digit += 1

ProcessingCard = CardNumber

while True:
    if ProcessingCard <= 0:
        break

    LastDigit = int(ProcessingCard % 10)
    Sum += LastDigit
    ProcessingCard = int(ProcessingCard / 100)

ProcessingCard = CardNumber / 10

while True:
    if ProcessingCard <= 0:
        break

    LastDigit = int(ProcessingCard % 10)
    Sum += int(((LastDigit * 2) % 10) + ((LastDigit * 2) / 10))
    ProcessingCard = int(ProcessingCard / 100)

divisor = 10

for i in range(digit - 2):
    divisor *= 10

FirstDigit = int(CardNumber / divisor)
divisor = divisor / 10
FirstTwoDigits = int(CardNumber / divisor)

if (int(Sum % 10) == 0):
    if (FirstDigit == 4 and (digit == 13 or digit == 16)):
        print("VISA")
    elif ((FirstTwoDigits == 34 or FirstTwoDigits == 37) and digit == 15):
        print("AMEX")
    elif ((FirstTwoDigits > 50 and FirstTwoDigits < 56) and digit == 16):
        print("MASTERCARD")
    else:
        print("INVALID")
        print(f"{FirstTwoDigits} {digit}")
else:
    print("INVALID")