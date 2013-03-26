def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    
    return len(dna)


def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''

    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''

    return dna2 in dna1


def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the DNA sequence dna is valid (that is, 
    it contains only nucleotide characters: 'A', 'T', 'C' and 'G'). 

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('TCATGT')
    True
    >>> is_valid_sequence('AGCTAC')
    True
    >>> is_valid_sequence('aAGcTAC')
    False
    >>> is_valid_sequence('ATHCDC')
    False

    '''

    for char in dna:
        if char not in 'ATCG':
            return False

    return True


def insert_sequence(dna1, dna2, index):
    ''' (str, str, int) -> str

    Return the DNA sequence dna1 obtained by inserting the second DNA 
    sequence dna2 into the first DNA sequence at the given index. 
    (You can assume that the index is valid.)
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 1)
    'CATCGG'
    >>> insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'
    
    '''

    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nuc):
    ''' (str) -> str
    
    Return the nucleotide's complement of the nucleotide nuc. 

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'

    '''

    if nuc == 'A':
        return 'T'
    elif nuc == 'T':
        return 'A'
    elif nuc == 'C':
        return 'G'
    elif nuc == 'G':
        return 'C'


def get_complementary_sequence(dna):
    ''' (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence dna. 

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('GCGCATTA')
    'CGCGTAAT'

    '''

    complementary_sequence = ''
    for char in dna:
        complementary_sequence = complementary_sequence + get_complement(char)

    return complementary_sequence

#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()


