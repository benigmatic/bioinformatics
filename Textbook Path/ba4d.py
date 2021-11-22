#Compute the Number of Peptides of Given Total Mass 

mass = [57,71,87,97,99,101,103,113,114,115,128,129, 131,137,147,156,163,186]
def Count(m):
    temp=[]    
    for i in range(m+1):
        res=0
        for j in mass:
            mass_left=i-j
            if mass_left==0:
                res+=1
            elif mass_left>0:
                res+=temp[mass_left]
        temp.append(res)
       
    return res
    

if __name__ == "__main__":
    input = "".join(open('input.txt')).split()
    # read input
    m = int(input[0])
   
    res = Count(m)
    print(res)