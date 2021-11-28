#Trim a Peptide Leaderboard 
AminoAcid = ['G','A','S','P','V','T','C','I','L','N','D','K','Q','E','M','H','F','R','Y','W']
AminoAcidMass = [57,71,87,97,99,101,103,113, 113,114,115,128, 128,129, 131,137,147,156,163,186]
def LinearSpectrum(peptide):
        prefixMass  = [0]*len(peptide)
        for i in range(len(peptide)):
            for j in range(20):
                if AminoAcid[j] == peptide[i]:
                    prefixMass[i] = prefixMass[i-1] + AminoAcidMass[j]
        LinearSpectrum = []
        LinearSpectrum.append(0)
        for i in range(len(peptide)):
            for j in range(i+1,len(peptide)):
                LinearSpectrum.append(prefixMass[j]-prefixMass[i])
        for element in prefixMass:
            LinearSpectrum.append(element)
        return sorted(LinearSpectrum)
def LinearScore (t_spectrum, spectrum):
    score = 0
    mass = list(set(spectrum+t_spectrum))
    for m in mass:
        score += min(t_spectrum.count(m),spectrum.count(m))     

   
    return score
def TRIM(Leaderboard, Spectrum, N):
    LinearScores = []
    res = []
    for j in range (len(Leaderboard)):
        peptide = Leaderboard[j]
        theoreticalSpectrum = LinearSpectrum(peptide)
        LinearScores.append(LinearScore(theoreticalSpectrum, Spectrum))
    for i in range (N):
        # move top N scores to result
        index = LinearScores.index(max(LinearScores))
        maxScore = LinearScores[index]
        res.append(Leaderboard[index])
        Leaderboard.pop(index)
        LinearScores.pop(index)
        while maxScore in LinearScores:
            index = LinearScores.index(max(LinearScores))
            res.append(Leaderboard[index])
            Leaderboard.pop(index)
            LinearScores.pop(index)
        
    return res
if __name__ == "__main__":
    input = "".join(open('input.txt')).split()
    # read input
    Leaderboard = []
    Spectrum = []
    N = 0
    for i in range(len(input)):
        
        if input[i].isdigit():
            Spectrum.append(int(input[i]))
        else:
            Leaderboard.append(input[i])
    N = Spectrum[-1]
    Spectrum = Spectrum[:-1] 
    
    res = TRIM (Leaderboard, Spectrum, N)

    print(*res)