data= {
    'G':'57', 'A':'71', 'S':'97', 'V':'99', 'T':'101', 'C':'103', 'I':'113',
    'L':'113', 'N':'114','D':'115', 'K':'128', 'Q':'128', 'E':'129',
    'M':'131', 'H':'137', 'F':'147', 'R':'156', 'Y':'163', 'W':'186'
}
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
if __name__ == "__main__":
    input = "".join(open('input.txt')).split()
    # read input
    peptide = input[0]
   
    res = Cyclospectrum(peptide)
    print(*res)