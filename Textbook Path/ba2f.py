from random import randint
from random import random
import numpy as np
#RandomizedMotifSearch
def PROFILE(motif):
    
    t = len(motif)
    k = len(motif[0])
    profile = {0: [0]*k, 1: [0]*k, 2: [0]*k, 3: [0]*k}
    # increment profile for each letter in mtif accordingly
    for i in range(k):
        for j in range(t):
            if motif[j][i]== 'A':
                profile[0][i] +=1
            elif motif[j][i]== 'C':
                profile[1][i] +=1
            elif motif[j][i]== 'G':
                profile[2][i] +=1
            elif motif[j][i]== 'T':
                profile[3][i] +=1
    #Laplace's Rule of Sucession
    for i in range(k):
        for j in range(4):
            profile[j][i] +=1
    return profile


   
def SCORE(Motifs):
    total = ''
    # created PROFILE for given Motifs
   
    profile = PROFILE(Motifs)
    k = len(Motifs[0])
    # Create the consensus string by checking which ATCG is the most frequent in the PROFILE for each i
    for i in range(k):
        biggest = 0
        for j in [0, 1, 2, 3]:
            if profile[j][i] > biggest:
                biggest = profile[j][i]
                if j==0: 
                    a = 'A'
                elif j==1:
                    a = 'C'
                elif j ==2:
                    a = 'G'
                elif j == 3:
                    a = 'T'
        total += a
    score = 0
    
    # sums up all HumminDistances for each motif. If letter is not the same as consensus string its being added to score fro all indexed of each motif
    for motif in Motifs:
        dist = np.zeros(len(total))
        for i in range (len(total)):
            if total[i]!= motif[i]:
                score = score +1
            
    
    return score
def MOTIFS(PROFILE,dna,k):
    
    newMotifs = []
    
    total = PROFILE[0][0] + PROFILE[1][0] + PROFILE[2][0] + PROFILE[3][0]
    for genome in dna:
        prob = []
        motifs = []
        for i in range(len(genome)-k+1):
            motif = genome[i:i+k]
            motifs.append(motif)
            propability = 1.0
            for j in range(len(motif)):
                if motif[j] == 'A':
                    val = 0
                elif motif[j] == 'C':
                    val = 1
                elif motif[j] == 'G':
                    val = 2
                elif motif[j] == 'T':
                    val = 3
                propability = propability *(float(PROFILE[val][j]) / total )
            prob.append(propability)
        
        prob = np.array(prob)
        idx = np.where(prob == prob.max())
        idx = idx[0][0]
        newMotifs.append(motifs[idx])
    
    return newMotifs
    
def RandomizedMotifSearch(dna,k,t):
    Bestmotifs = []
    Motifs = []
    for motif in dna:
        rand = randint(0, len(motif)-k)
        newMotif = motif[rand:rand+k]
        Motifs.append(newMotif)
    Bestmotifs = Motifs
    
    while (1==1):
        profile = PROFILE(Motifs)
        
        
        Motifs = MOTIFS(profile, dna,k)
        if SCORE(Motifs) < SCORE (Bestmotifs):
            Bestmotifs = Motifs
        else:
            return Bestmotifs
        
    return Bestmotifs
def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    # read input
    k = int(input[0])
    d = int(input[1])
    dna = input[2:]

    min = 1e6
    for i in range(1000):
        res = RandomizedMotifSearch(dna, k, d)
        #compare the scores from each random start and select the lowest for motifs produced
        resScore = SCORE(res)
        if resScore < min:
            min = resScore
            result = res
    
    
    print("\n".join(result))
 

if __name__ == "__main__":
    main()
