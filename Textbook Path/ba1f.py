#Finda Position in a genome Minimizing the Skew
import numpy as np
def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    genome = input[0]
    indices = []
    c_count = 0
    g_count = 0
    min = 0
    cur_index = 0
    for i in range (len(genome)):
        cur_index += 1
        if genome[i]== 'C':
            c_count +=1
        if genome[i]=='G':
            g_count +=1
        skew = g_count - c_count
        
        if skew < min:
            
            indices = [cur_index]
            min = skew
        if skew==min and cur_index not in indices:
            indices.append(cur_index)
        
    
    
    print(*indices) 
if __name__ == "__main__":
  main()
