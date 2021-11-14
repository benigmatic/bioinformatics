#Implement DistanceBetweenPatternAndStrings
def DistanceBetweenPatternAndString(pattern, dna):
    distance = 0
    k = len(pattern)
    for string in dna:
        HDist = float("inf")
        for i in range(len(string)-k+1):
            kmer = string[i:i+k]
            if HDist > HammingDistance(pattern,kmer):
                HDist = HammingDistance(pattern, kmer)
        distance = distance + HDist
            
    return distance
def HammingDistance(str1, str2):
    count = 0
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            count += 1
    return count

def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    # read input
    pattern = input[0]
    
    dna = input[1:]
    distance = DistanceBetweenPatternAndString(pattern, dna)
    print(distance)


if __name__ == "__main__":
    main()
