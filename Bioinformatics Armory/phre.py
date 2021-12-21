# Read Quality Distribution
from Bio import SeqIO

def average(m):
	return float(sum(m))/(len(m))

def qthreshold(threshold, fastq):
	# Create handle
	handle = SeqIO.parse(fastq, "fastq")

	
	count = 0
	for record in handle:
		if average(record.letter_annotations["phred_quality"]) < threshold:
			count += 1

	return count
def qdist(threshold, fastq):
	handle = SeqIO.parse(fastq,"fastq")
	print(handle)
if __name__ == "__main__":
	# input.fastq file should be in the same directory
	# number is the threshold
    print (qthreshold(21, "input.fastq"))
    