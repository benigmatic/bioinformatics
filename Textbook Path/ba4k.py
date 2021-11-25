#Compute the Score of a Linear Peptide  
AminoAcid = ['G','A','S','P','V','T','C','I','L','N','D','K','Q','E','M','H','F','R','Y','W']
AminoAcidMass = [57,71,87,97,99,101,103,113, 113,114,115,128, 128,129, 131,137,147,156,163,186]
def LinearSpectrum(Peptide):
        prefixMass  = [0]*len(peptide)
        for i in range(len(Peptide)):
            for j in range(20):
                if AminoAcid[j] == Peptide[i]:
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
if __name__ == "__main__":
    input = "".join(open('input.txt')).split()
    # read input
    peptide = input[0]
    spectrum = input[1:]
    spectrum = [int(spectrum[i]) for i in range(len(spectrum))]
    theoreticalSpectrum = LinearSpectrum(peptide)
    res = LinearScore(theoreticalSpectrum, spectrum)
    print(res)