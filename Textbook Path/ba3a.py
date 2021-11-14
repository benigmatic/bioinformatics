#Generate the k-mer Composition of a String
def StringComposition(k,text):
    result = []
    
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        if kmer not in result:
            result.append(kmer)
   
    
    return sorted(result)   
def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    # read input
    k = int(input[0])
    text = input[1]
    
    res = StringComposition(k,text)
    print("\n".join(res))
if __name__ == "__main__":
  main()