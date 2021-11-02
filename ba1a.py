#Compute the Number of Times a Pattern Appears in a Text

def main():
    # reads input from terminal
    text = input("Enter DNA String:")
    print(text)
    pattern = input("Enter the Pattern to search for:")
    print(pattern)
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    print(count)
if __name__ == "__main__":
  main()
