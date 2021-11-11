#Find a Median String
import itertools
def HammingDistance(str1, str2):
    count = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return(count)


def MinHammingDistance(pattern, text):
    min = float("inf")
    for i in range(len(text) - len(pattern) + 1):
        distance = HammingDistance(pattern, text[i:i+len(pattern)])
        if distance < min:
            min = distance
    return min

def Generate_kmers(k):
    bases = ['A', 'C', 'G', 'T']
    res = [''.join(p) for p in itertools.product(bases, repeat=k)]
    return res

def Median(k, dna):
    kmers = Generate_kmers(k)
    min = float("inf")
    res = ""
    for kmer in kmers:
        dist = 0
        for i in range(len(dna)):
            dist += MinHammingDistance(kmer, dna[i])
              
        if dist <= min:
            min = dist
            res = kmer
               
    return res

if __name__ == "__main__":
        # reads input from terminal
    input = "".join(open('input.txt')).split()
    # read input
    k = int(input[0])    
    dna = input[2:]
    res = Median(k, dna)
    print(res)