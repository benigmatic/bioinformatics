#Length of a Longest Path in the Manhattan Tourist Problem
def LongestPath(n,m,down,right):
    
    s = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range (1,n+1):
        s[i][0] = s[i-1][0]+down[i-1][0]
    
    for j in range (1,m+1):
        s[0][j] = s[0][j-1]+right[0][j-1]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i-1][j]+down[i-1][j], s[i][j-1]+ right[i][j-1])
    return s[n][m]
if __name__ == "__main__":
    input = "".join(open('input.txt')).splitlines()
    NM = input[0].split(" ")
    n =int(NM[0])
    m = int (NM[1])
   
    Down = []
    index = 1
    for i in range(n):
        vals =input[i+1].split()        
        vals = [int(vals[i]) for i in range(len(vals))]
        Down.append(vals)
        index = index+1
    Right= []
    
    for i in range(index, index+ n+1):

        vals =input[i+1].split()        
        vals = [int(vals[i]) for i in range(len(vals))]
        
        Right.append(vals)
    
    res = LongestPath(n,m,Down,Right)
    print(res)
