#Generate the d-Neighborhood of a String
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

def main():
    input = "".join(open('input.txt')).split()
    # read input
    pattern = (input[0])
    d = int (input[1])    
    res = Neighbors(pattern,d)
    
    with open('output.txt', 'w') as f:
        for i in res:
            f.write(i)
            f.write('\n')
    print("DONE")           

if __name__ == "__main__":
  main()
