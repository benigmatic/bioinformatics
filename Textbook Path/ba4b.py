#Find Substrings of a Genome Encoding a Given Amino Acid String


def table():
    codons = dict()
    # A
    codons['AUG'] = 'M'
    codons['AUA'] = 'I'
    codons['AUC'] = 'I'
    codons['AUU'] = 'I'
    codons['AGG'] = 'R'
    codons['AGA'] = 'R'
    codons['AGC'] = 'S'
    codons['AGU'] = 'S'
    codons['ACG'] = 'T'
    codons['ACA'] = 'T'
    codons['ACC'] = 'T'
    codons['ACU'] = 'T'
    codons['AAG'] = 'K'
    codons['AAA'] = 'K'
    codons['AAC'] = 'N'
    codons['AAU'] = 'N'
    #C
    codons['CAU'] = 'H'
    codons['CAC'] = 'H'
    codons['CAA'] = 'Q'
    codons['CAG'] = 'Q'
    codons['CCU'] = 'P'
    codons['CCC'] = 'P'
    codons['CCA'] = 'P'
    codons['CCG'] = 'P'
    codons['CGU'] = 'R'
    codons['CGC'] = 'R'
    codons['CGA'] = 'R'
    codons['CGG'] = 'R'
    codons['CUU'] = 'L'
    codons['CUC'] = 'L'
    codons['CUA'] = 'L'
    codons['CUG'] = 'L'
    #G
    codons['GAU'] = 'D'
    codons['GAC'] = 'D'
    codons['GAA'] = 'E'
    codons['GAG'] = 'E'
    codons['GCU'] = 'A'
    codons['GCC'] = 'A'
    codons['GCA'] = 'A'
    codons['GCG'] = 'A'
    codons['GGU'] = 'G'
    codons['GGC'] = 'G'
    codons['GGA'] = 'G'
    codons['GGG'] = 'G'
    codons['GUU'] = 'V'
    codons['GUC'] = 'V'
    codons['GUA'] = 'V'
    codons['GUG'] = 'V'
    #U
    codons['UAU'] = 'Y'
    codons['UAC'] = 'Y'
    codons['UAA'] = '*'
    codons['UAG'] = '*'
    codons['UCU'] = 'S'
    codons['UCC'] = 'S'
    codons['UCA'] = 'S'
    codons['UCG'] = 'S'
    codons['UGU'] = 'C'
    codons['UGC'] = 'C'
    codons['UGA'] = '*'
    codons['UGG'] = 'W'
    codons['UUU'] = 'F'
    codons['UUC'] = 'F'
    codons['UUA'] = 'L'
    codons['UUG'] = 'L'

    return codons


def Complement(dna):
    lookup_dict = {"A":"T", "C":"G", "G":"C", "T":"A"}
    reverse_compl = ""
    length = len(dna)
    for index in range(length):
        reverse_compl += lookup_dict[dna[index]]

    return reverse_compl[::-1]


def toPeptide(rna):
    peptide = ''
    t = table()

    for start in range(0, len(rna) - 2, 3):
        if t[rna[start: start + 3]] == "*":
            break

        peptide += t[rna[start: start + 3]]

    return peptide


def toRna(dna):
    res = dna.replace("T","U")
    return res


def toDna(rna):
    res = rna.replace("U","T")
    return res


def substrs_in_genome(dna, peptide):
    res = []
    rna = toRna(dna)
    complement_rna = toRna(Complement(dna))
    k = len(peptide)*3
    i = 0
    while i + k <= len(dna):
        substring1 = rna[i: i + k]
        substring2 = complement_rna[i: i + k]
        if peptide == toPeptide(substring1):
            res.append(toDna(substring1))

        if peptide == toPeptide(substring2):
            res.append(Complement(toDna(substring2)))

        i += 1

    return res


if __name__ == "__main__":
    input = "".join(open('input.txt')).split()
    # read input
    dna = input[0]
    peptide = input[1]
    res = substrs_in_genome(dna, peptide)
    for element in res:
        print(element)
