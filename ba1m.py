def numbertopattern(index,k):
    reversestring = ''
    l = ['A','C','G','T']
    for i in range(k):
        letter = int(index % 4)
        reversestring += l[letter]
        index = (index - letter)/4
    return reversestring[::-1]


def main():
    input = "".join(open('input.txt')).split()
    # read input
    index = int (input[0])
    k = int (input[1])    
    print(numbertopattern(index,k))
if __name__ == "__main__":
  main()