#Probability of a Hidden Path Problem
import numpy as np


def PathProbability(path, HMM):
    prob = 0.5
    index1 = 0
    index2 = 0
    
    for i in range (len(path)-1):
        
        if path[i] == "A":
            index1 = 0
        else:
            index1 = 1
        if path[i+1] == "A":
            index2 = 0
        else:
            index2 = 1
        
        prob *= HMM[index1][index2]
    return prob
def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    # read input
    path = (input[0])
    states = input[2]
    states2 = input[3]
    
    
    HMM = []
    val = [float(input[8]), float(input[9])]
    HMM.append(val)
    val = [float(input[11]), float(input[12])]
    HMM.append(val)
    print(HMM)
    res = PathProbability(path, HMM)
    print(res)
if __name__ == "__main__":
  main()
