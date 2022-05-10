from Bio.Seq import Seq
from Bio import SeqIO

def gene_ORFs(s):
    s = Seq(s)
    s_reverse = s.reverse_complement()


    proteins = []
    proteins.extend(str(s.translate()).split("*"))
    proteins.extend(str(s[1:].translate()).split("*"))
    proteins.extend(str(s[2:].translate()).split("*"))
    proteins.extend(str(s_reverse.translate()).split("*"))
    proteins.extend(str(s_reverse[1:].translate()).split("*"))
    proteins.extend(str(s_reverse[2:].translate()).split("*"))

    orfs = sorted([i[i.find("M"):] for i in proteins if "M" in i], key= lambda x: len(x), reverse=True)
    print(orfs[0])
    return orfs

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        dna = f.readline().strip()
    gene_ORFs(dna)