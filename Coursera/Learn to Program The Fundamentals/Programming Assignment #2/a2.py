def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    if dna == '' and nucleotide == '':
        return 0
    
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna1.count(dna2) >= 1

def is_valid_sequence(dna):
    """ (str) -> bool

    Returns whether or not the dna sequence being passed in is valid.
    Determines this by checking if it contains any other character rather than ATCG

    >>> is_valid_sequence('ATCGATCG')
    True

    >>> is_valid_sequence('IMNOTVALID')
    False
    
    """

    for char in dna:
        if char in "ATCG":
            continue

        else:
            return False
    
    return True

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Inserts the string of dna2 into dna1 at the specified index

    Precondition: index is valid, not out of bounds

    >>> insert_sequence("CCGG", "AT", 2)
    "CCATGG"

    >>> insert_sequence("CTGA", "CT", 1)
    "CCTTGA"

    """
    
    return dna1[:index] + dna2 + dna1[index:]
        
def get_complement(nucleotide):
    """ (str) -> str

    Precondition: Assumes that the nucleotide passed in is always one of "ATCG"

    Returns the compelement of the nucleotide

    A -> T
    C -> G
    T -> A
    G -> C
    
    >>> get_complement("A")
    "T"

    >>> get_complement("C")
    "G"

    """

    if nucleotide == '':
        return ''
    
    strand = "ACTG"
    
    return strand[(strand.find(nucleotide) + 2) % 4]


def get_complementary_sequence(dna):
    """ (str) -> str

    Precondition: Assumes that the DNA sequence passed in only contains "ATCG"

    >>> get_complementary_sequence("AT")
    "TA"

    >>> get_complementary_sequence("ATCG")
    "TAGC"

    """
    
    complement_dna = ''
    
    for char in dna:
        complement_dna += get_complement(char)

    return complement_dna
