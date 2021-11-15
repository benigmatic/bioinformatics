#Construct the De Bruijn Graph of a Collection of k-mers
def Graph(kmers):
    result = {}
    n = len(kmers)
    for i in range(n):
        # get the prefix of the current k-mer
        suffix = kmers[i][1:] 
        prefix =kmers[i][:-1]
        if prefix in result:
            result[prefix].append(suffix)
        else:
            result[prefix] = [suffix]  

    return result
def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    
    text = input[0:]
    
    res = Graph(text)
    print(res)
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