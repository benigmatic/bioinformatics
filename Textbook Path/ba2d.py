import numpy as np 
# Greedy Motif Search

def SymbolToNumber(Symbol):

    if Symbol == "A":
        return 0
    elif Symbol == "C":
        return 1
    elif Symbol == "G":
        return 2
    elif Symbol == "T":
        return 3


def NumberToSymbol(index):

    if index == 0:
        return str("A")
    elif index == 1:
        return str("C")
    elif index == 2:
        return str("G")
    elif index == 3:
        return str("T")


def HammingDistance(str1, str2):
    count = 0
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            count += 1
    return count


def window(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i+k]


def ProfileMostProbable(Text, k, Profile):

    letter = [[] for key in range(k)]
    probable = ""
    hamdict = {}
    index = 1
    for a in range(k):
        for j in "ACGT":
            letter[a].append(Profile[j][a])
    for b in range(len(letter)):
        number = max(letter[b])
        probable += str(NumberToSymbol(letter[b].index(number)))
    for c in window(Text, k):
        for x in range(len(c)):
            y = SymbolToNumber(c[x])
            index *= float(letter[x][y])
        hamdict[c] = index
        index = 1
    for pat, ham in hamdict.items():
        if ham == max(hamdict.values()):
            final = pat
            break
    return final


def Count(Motifs):

    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for i in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def FindConsensus(motifs):

    consensus = ""
    for i in range(len(motifs[0])):
        countA, countC, countG, countT = 0, 0, 0, 0
        for motif in motifs:
            if motif[i] == "A":
                countA += 1
            elif motif[i] == "C":
                countC += 1
            elif motif[i] == "G":
                countG += 1
            elif motif[i] == "T":
                countT += 1
        if countA >= max(countC, countG, countT):
            consensus += "A"
        elif countC >= max(countA, countG, countT):
            consensus += "C"
        elif countG >= max(countC, countA, countT):
            consensus += "G"
        elif countT >= max(countC, countG, countA):
            consensus += "T"
    return consensus


def ProfileMatrix(motifs):

    Profile = {}
    A, C, G, T = [], [], [], []
    for j in range(len(motifs[0])):
        countA, countC, countG, countT = 0, 0, 0, 0
        for motif in motifs:
            if motif[j] == "A":
                countA += 1
            elif motif[j] == "C":
                countC += 1
            elif motif[j] == "G":
                countG += 1
            elif motif[j] == "T":
                countT += 1
        A.append(countA)
        C.append(countC)
        G.append(countG)
        T.append(countT)
    Profile["A"] = A
    Profile["C"] = C
    Profile["G"] = G
    Profile["T"] = T
    return Profile


def Score(motifs):

    consensus = FindConsensus(motifs)
    score = 0.0000
    for motif in motifs:
        score += HammingDistance(consensus, motif)
    
    return round(score, 4)
def GreedyMotifSearch(DNA, k, t):
  
    import math
    bestMotifs = []
    bestScore = math.inf
    for string in DNA:
        bestMotifs.append(string[:k])
    base = DNA[0]
    for i in window(base, k):
       
        newMotifs = [i]
        
        for j in range(1, len(DNA)):
           
            profile = ProfileMatrix(newMotifs)
            probable = ProfileMostProbable(DNA[j], k, profile)
            newMotifs.append(probable)

        if Score(newMotifs) < bestScore:
       
            bestScore = Score(newMotifs)
            bestMotifs = newMotifs
    return bestMotifs
def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    # read input
    k = int(input[0])
    t = int(input[1])
    dna = input[2:]

    bestMotifs = GreedyMotifSearch(dna, k, t)
    print(*bestMotifs)


if __name__ == "__main__":
    main()
