
from Bio import SeqIO

with open("input.txt", "r") as input_data:
    dna = [fasta.seq for fasta in SeqIO.parse(input_data, 'fasta')]

# To find out r use LALIGN tool
# Link :https://www.ebi.ac.uk/Tools/psa/lalign/
# Default parameters are used
# In the results search for a 100% match and use it as r

r = 'AACAGATTGAGATCCGACCTTTGTCGAAGGCATCGCTG'




def HammingDistance(string1, string2):
        dist = 0
        for a, b in zip(string1, string2):
                if a != b:
                        dist += 1
        return dist
for x in range(0, 2):
    count = 0
    stringx = dna[x]
    for i in range(0, len(stringx)-len(r)):
        string = stringx[i:i+len(r)]
        if HammingDistance(r, string) <= 3:
            count += 1
    print (count)
