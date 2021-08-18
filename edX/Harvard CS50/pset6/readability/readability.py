from cs50 import get_string


def main():
    Input = get_string("Text: ")

    Length = len(Input)

    letters = 0
    words = 0
    sentences = 0

    for i in range(Length):
        if str.isalpha(Input[i]) == True:
            letters += 1
        elif Input[i] == "!" or Input[i] == "." or Input[i] == "?":
            sentences += 1
        elif Input[i] == " ":
            words += 1

    words += 1

    level = round(index((letters / float(words) * 100), sentences / float(words) * 100))

    if level < 1:
        print("Before Grade 1")
    elif level > 16:
        print("Grade 16+")
    else:
        print(f"Grade {level}")

    return


def index(L, S):

    answer = float(0.0588 * L) - (0.296 * S) - 15.8
    return answer


main()