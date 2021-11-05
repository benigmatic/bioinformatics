def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    pattern = input[0]
    text = input [1]
    d = input [2]
    d = int (d)
    indices = []
    length = len(text)- len(pattern)+1
    for i in range (length):

        substr = text[i: i+len(pattern)]
        dist = HammingDistance(pattern, substr)
        if dist <= d :
            indices.append(i)
    print(*indices)
def HammingDistance(str1, str2):
    count = 0
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            count += 1
    return(count)
if __name__ == "__main__":
  main()