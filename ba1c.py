#Compute the Number of Times a Pattern Appears in a Text

def main():
    # reads input from terminal
    text = input("Enter DNA String:")
    
    reverse = ""
    for i in text :
        if i == 'A':
            reverse = "T" + reverse
        elif i == 'T':
            reverse = "A" + reverse
        elif i == 'G':
            reverse = "C" + reverse
        else :
            reverse = "G" + reverse
    
    print(reverse)
if __name__ == "__main__":
  main()
