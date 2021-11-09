#Find All Occurrences of a Pattern in a String
import numpy as np
def main():
    # reads input from terminal
    kmer = input("k-mer:")
    indices = []
    text = input("Enter DNA String:") 
    k = len(kmer)
    length = len(text)
    for i in range (0, len(text)- len(kmer)+1):
        if text[i:i+k] == kmer:
         indices.append(i)
    indices = np.array(indices)
    print(indices) 
if __name__ == "__main__":
  main()
