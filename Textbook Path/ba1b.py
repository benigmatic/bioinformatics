#Find the Most Frequent Words in a String

def main():
    # reads input from terminal
    text = input("Enter DNA String:")
    print(text)
    k = input("k (length of the k-mer):")
    k = int (k)
    patterns = []
    counts = CountDict(text, k)
    m = max(counts.values())
    for i in counts:
        if counts[i] == m:
            patterns.append(text[i:i+k])
    patterns2 = remove_duplicates(patterns)
    for i in range (0, len(patterns2)):
        print(patterns2[i])
    
def remove_duplicates(Text):
    arr = [] # output variable
    for i in Text:
        if not i in arr:
            arr.append(i)
    return arr

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Text, Pattern)
    return Count

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
if __name__ == "__main__":
  main()
