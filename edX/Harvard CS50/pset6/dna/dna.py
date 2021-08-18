from sys import argv


def main():

    # Fail check
    if len(argv) != 3:
        print("Usage: python dna.py {data.csv} {sequence.txt}")
        return 1

    strands = []
    people = {}

    # Opening the csv file containing data
    data = open(argv[1], "r")

    # For each row, index and row both iterates
    for index, row in enumerate(data):
        if index == 0:
            # Skip first line, scans for the strands
            strands = [strand for strand in row.strip().split(",")][1:]
        else:
            # Scanning in people
            currentRow = row.strip().split(",")
            people[currentRow[0]] = [int(x) for x in currentRow[1:]]

    # Opening the txt file for checkup
    dnaStrand = open(argv[2], "r")

    # https://stackoverflow.com/questions/48715691/python-object-of-type-io-textiowrapper-has-no-len, solved the problem of comparing len of dnaStrands
    dnaStrand = dnaStrand.read()

    finalStrands = []

    for strand in strands:

        i = 0
        maxStrand = -1
        currentMax = 0

        while i < len(dnaStrand):

            # Slicing the text by i units
            currentSlice = dnaStrand[i:i + len(strand)]

            if currentSlice == strand:
                currentMax += 1
                maxStrand = max(maxStrand, currentMax)
                i += len(strand)  # Move the index up by length of the correct strand

            else:
                currentMax = 0  # Reset current max
                i += 1

        # Final strands with max strand of each loop, updated to the list of final Strands
        finalStrands.append(maxStrand)

    # Debug use
    # print(strand)
    # print(people)
    # print(finalStrands)

    # Iterate through all people to check if the dna strands are same
    for name, dna in people.items():
        if dna == finalStrands:
            print(name)
            return

    # Print no match if data does not match
    print("No match")

    return


main()
