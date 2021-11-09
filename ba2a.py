# Implement Motif Enumeration
def HammingDistance(str1,str2):
    count = 0
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            count += 1
    return(count)
def Neighbors(pattern, d):
    nucleotides = ['A','C','G','T']
    if d == 0:
        return pattern
    if (len(pattern)==1):
        return nucleotides
    Neighborhood = []
    SuffixNeighbors = Neighbors(pattern[1:],d)
    for text in SuffixNeighbors:
        
        if HammingDistance(pattern[1:],text)<d:
            for i in nucleotides:
                Neighborhood.append(i+text)
        else :
            Neighborhood.append(pattern[0]+ text)
    return Neighborhood
def MotifEnumeration(dna, k,d):
    patterns = set()    
    for i in range(len(dna[0]) - k + 1):
            kmer = dna[0][i:i+k]
            neighbors = Neighbors(kmer,d)
            for pattern in neighbors:
                for z in dna:
                    count =0 
                    for j in range(len(z)-k+1):
                        if HammingDistance(pattern, z[j:j+k]) <=d:
                            count =1
                    if count ==0: 
                        break
                if count == 1:
                    patterns.add(pattern)    
    return patterns

def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    # read input
    k = int (input[0])
    d = int (input[1])
    dna = input[2:]
    
    patterns = MotifEnumeration (dna,k,d)
    print(*patterns)

if __name__ == "__main__":
  main()