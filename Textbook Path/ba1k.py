
import numpy as np
from numpy.core.arrayprint import array2string
vals = {'A':0, 'C':1, 'G':2, 'T':3}
def PatternToNumber (str):
    count =0
    for i in range(0,len(str)):
        count+= vals[str[i]]*pow(4,len(str)-i-1)
    return(count)
def main():
    input = "".join(open('input.txt')).split()
    # read input
    
    
    text = input[0]
    k = int (input[1])
    array = []
    for i in range(pow(4,k)):
        array.append(0)
    for i in range(len(text)-k+1):
        num = PatternToNumber (text[i:i+k])
        array[num] = array[num]+1
    
    print(*array)
    """
    letters = ['A','C','G','T']
    for i in range (len(letters)):
        for j in range(len(letters)):
            
            kmer[letters[i]+letters[j]] = 0
            count+=1
            perms.append(letters[i]+letters[j])
    for i in range(len(text)-k+1):
        cur_kmer = text[i:i+k]
        kmer[cur_kmer]= kmer[cur_kmer] + 1
    print(*kmer.values())
    """
    
if __name__ == "__main__":
  main()
