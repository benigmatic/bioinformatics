#Compute the Score of a Cyclic Peptide Against a Spectrum
data= {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 
'H': 137, 'K': 128, 'M': 131,'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 
'R': 156, 'T': 101, 'V': 99, 'Y': 163, 'W': 186}
def peptideCombo(peptide):
	combo = []
	
    
	for i in range(0, len(peptide)): #linear subpeptides
		for j in range(i, len(peptide)):
			combo.append(peptide[i:j + 1])
	for i in range(2, len(peptide)): #cyclic subpeptides
		for j in range(0, i- 1):
			combo.append(peptide[i:len(peptide)] + peptide[0:j+ 1])
	
	
	return combo
def Cyclospectrum (peptide):
    
    res = []
    
    l = peptideCombo(peptide)
    for el in l:
        
        val = 0
        for i in el:
            
            val = val + int(data[i])
        res.append(val)
    res.append(0)
    res.sort()
    
    return res 
def CycloPeptideScoring(peptide, spectrum):
    
    peptide_spectrum = Cyclospectrum(peptide)
    print(spectrum)
    print(peptide_spectrum)
    score = 0
    mass = list(set(spectrum+peptide_spectrum))
    print(mass)
    for m in mass:
        score += min(peptide_spectrum.count(m),spectrum.count(m))     

   
    return score
if __name__ == "__main__":
    input = "".join(open('input.txt')).split()
    # read input
    peptide = input[0]
    spectrum = input[1:]
    spectrum = [int(spectrum[i]) for i in range(len(spectrum))]
    res = CycloPeptideScoring(peptide, spectrum)
    print(res)
  