
### Base Filtration by Quality

from Bio import SeqIO

def BaseFiltrationQuality(data):
    records = []
    with open(data, "r") as f:
        t = int(f.readline().strip())
        for record in SeqIO.parse(f, "fastq"):
            phred = record.letter_annotations["phred_quality"]
            start, end = 0, len(phred)
            while phred[start] < t:
                start += 1
            while phred[end-1] < t:
                end -= 1
            records.append(record[start:end].format('fastq'))
    return records

if __name__ == "__main__":
    data = "input.fastq"
    res = BaseFiltrationQuality(data)
    print(res)
    with open('output.txt', 'w') as f:
     f.writelines(res)
