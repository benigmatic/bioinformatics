#Find a Profile-most Probable k-mer in a String
def CALC_PROFILE(profile, kmer):
    
    prob = 1.0
    
    for i in range (len(kmer)):
        
        if kmer[i]=="A":
            prob = prob * float(profile[0][i])
        elif kmer[i] == "C":
            prob = prob * float(profile[1][i])
        elif kmer[i] == "G":
            prob = prob * float(profile[2][i])
        elif kmer[i] == "T":
            prob = prob * float(profile[3][i])
    
    return prob
def PROFILE(text,k,profile):
    max = 0.0
    res = ""
    for i in range(len(text)- k + 1):
        kmer = text[i:i+k]
        pr = CALC_PROFILE(profile, kmer)
        if pr> max:
            
            max = pr
            res = kmer
    return res 
if __name__ == "__main__":
        # reads input from terminal
    input = "".join(open('input.txt')).split()
    # read input
    dna = input[0]
    k = int(input[1])
    profile = []
    count = 0
    for i in range(4):
        arr = []
        for j in range(k):
            arr.append(input[2+count])
            count = count + 1
        profile.append(arr)
    
    res = PROFILE(dna,k,profile)
    print(res)