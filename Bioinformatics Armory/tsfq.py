from Bio import SeqIO

records = SeqIO.parse("input.fastq", "fastq")
count = SeqIO.write(records, "output.fasta", "fasta")
print("Converted %i records" % count)