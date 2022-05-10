from Bio import SeqIO
from Bio.Seq import Seq


def match_reverse(seqs):
    count = 0
    for seq in seqs:
        my_seq = Seq(seq)
        reverse_seq = my_seq.reverse_complement()
        if my_seq == reverse_seq:
            count += 1
    return count

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        seqs = [str(record.seq) for record in SeqIO.parse(f, "fasta")]
    count = match_reverse(seqs)
    print(count)