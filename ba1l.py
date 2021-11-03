def main():
    input = "".join(open('input.txt')).split()
    # read input
    vals = {'A':0, 'C':1, 'G':2, 'T':3}
    count = 0
    str = input[0]
    for i in range(0,len(str)):
        count+= vals[str[i]]*pow(4,len(str)-i-1)
    print(count)
if __name__ == "__main__":
  main()