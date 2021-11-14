# Reconstruct a String From its Genome Path
def Reconstruct(path):
    genome = path[0]
    for i in range (1, len(path)):
        genome = genome + path[i][len(path[0])-1]
    return genome
def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    # read input
    
    path = input[0:]
    
    res = Reconstruct(path)
    print(res)
if __name__ == "__main__":
  main()