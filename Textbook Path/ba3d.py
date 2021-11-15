#Construct the De Bruijn Graph of a String
def Graph (dna,k):
    result = {}
   
    for i in range(len(dna)-k+1):
        prefix = dna[i: i+k-1]
        suffix =dna[i+1: i+k]
        if prefix in result:
            result[prefix].append(suffix)
        else:
            result[prefix] = [suffix]
    return result
def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    k = int (input[0])
    text = input[1]
    
    res = Graph(text,k)
    
    with open("output.txt", "w") as external_file:
       
        for i in sorted (res):
            print(i,end="",file=external_file)
            print(" -> ", end="",file=external_file)
            for j in range(len(res[i])):
                if (j == len(res[i])-1):
                    print(res[i][j],file=external_file)
                elif (len(res[i])>1):
                    print(res[i][j],end=",",file=external_file)
                else : print(res[i][j],file=external_file)
        external_file.close()
        
    
if __name__ == "__main__":
  main()