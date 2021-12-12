# DNA stats
#Introduction to the Bioinformatics Armory 
#Download the BioPython from here https://biopython.org/wiki/Download
from Bio.Seq import Seq
if __name__ == "__main__":
    input = "".join(open('input.txt')).split()
    seq = str(input[0:])
    my_seq = Seq(seq)
    counts = []
    counts.append(my_seq.count("A"))
    counts.append(my_seq.count("C"))
    counts.append(my_seq.count("G"))
    counts.append(my_seq.count("T"))
    print(*counts)
