# Pseudocode taken from Chapter 2 GibbsSampler
import numpy as np
from random import randint
from random import random



def KmerPROFILE(PROFILE, motif ):
    L = len(motif)
    k = len(PROFILE[0])
    #print(k)
    probabilities = []

    total = PROFILE[0][0] + PROFILE[1][0] + PROFILE[2][0] + PROFILE[3][0]
    for i in range(L - k + 1):
        #calulate probabilities for each k-mer selected from motif
        kmer = motif[i:i + k]

        Prob = 1.0
        for j  in range (len(kmer)):

            if kmer[j] == 'A':
                num = 0
            elif kmer[j] == 'C':
                num = 1
            elif kmer[j] == 'G':
                num = 2
            elif kmer[j] == 'T':
                num = 3
            #Fprinprint(PROFILE[num][j])
            Prob *= float(PROFILE[num][j]) / total
        probabilities.append(Prob)
   # calulate the index of biased Dice
    index = DiceRoll(probabilities)
    # select ne motif at the new index
    newMotif = motif[index: index+k]
    return newMotif
    
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





def DiceRoll(prob):

    sum = []
    current =0
    for i in prob:
       current += i
       sum.append(current)
    index = random()* current
    for i in range (len(sum)):
        if index < sum[i]:
            return i
    
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

def GibbsSampler(genome, k, t, N):
    Motifs = []
    # randomly select k-mers Motifs in each string from DNA
    for motif in genome:
        rand = randint(0, len(motif) - k)
        newMotif = motif[rand:rand+k]
        Motifs.append(newMotif)
    BestMotifs = Motifs
    minScore = SCORE(BestMotifs)
    for a in range(N):
        # select random k-mer that won't be put into the profile
        rand = randint(0, t - 1)
        temp = []
        # create an array to pass all motifs but the randomly selected
        for i in range(len(Motifs)):
            if (i != rand):
                temp.append(Motifs[i])
       # Create a PROFILE for all motifs but the randomly ignored
        Profile = PROFILE(temp)
        # Profile-randomly generated k-mer in the rand-th sequence
        Motifs[rand] = KmerPROFILE(Profile, genome[rand])
        # Calculate the new Score
        curScore = SCORE(Motifs)
        # Compare the Score and save the lowest
        if minScore > curScore:
            minScore = curScore
            BestMotifs = Motifs
           
    return BestMotifs


def main():
    input = "".join(open('gibbs.txt')).split()
    # read input
    k = int(input[0])
    t = int(input[1])
    N = int(input[2])    
    genome = input[3:]
    # set Score to high value
    min = 1e6
    #random 20 starts
    for i in range(20):
        res = GibbsSampler(genome, k, t, N)
        #compare the scores from each random start and select the lowest for motifs produced
        resScore = SCORE(res)
        if resScore < min:
            min = resScore
            result = res
    
    print("\n".join(result))
if __name__ == "__main__":
  main()

   
    

    
