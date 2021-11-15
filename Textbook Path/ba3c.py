#Construct the Overlap Graph of a Collection of k-mers
def prefix(string):
    return string[:len(string)-1]


def suffix(string):
    return string[1:]


def overlap(patterns):
    
    l = len(patterns)
    pairs = {}
    for i in range(l):
        for j in range(l):            
            if (i != j) and (suffix(patterns[i]) == prefix(patterns[j])):
                pairs[patterns[i]] = patterns[j]
    return pairs

def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    #
    text = input[0:]
    
    res = overlap(text)
    
    for i in sorted (res) :
        print("%s -> %s"%(i, res[i]))
    
if __name__ == "__main__":
  main()