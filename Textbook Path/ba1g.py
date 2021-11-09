def main():
    input = "".join(open('input.txt')).split()
    # read input
    count = 0
    str1 = input[0]
    str2 = input[1]
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            count += 1
    print(count)
if __name__ == "__main__":
  main()
