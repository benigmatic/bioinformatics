import sys
def main():
    input = "".join(open('localAlignmentinput.txt')).split()
    # read input
    str1 = input[0]
    str2 = input[1]
    str1 =" "+ str1
    str2 = " "+str2
    # insertion/deletion penalty
    sigma = -5
    global_max = - 1000000 
    start_c = 0
    start_r = 0
    # saving SCORE matrix
    letters = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    SCORE = [] 
    with open("SCORE.txt", 'r') as f:
        for line in f.readlines():
            str = line.strip()
            arr = str.split()
            SCORE.append(arr)
    #Declaring an empty 2D arrays to kepp trackof backtrack path, and scores
    s = []
    backtrack = []
    #Declaring an empty 1D array.
    b = []
    b_backtrack  = []
    # initialize to 0s
    for col in range (len(str1)):
        col = []
        b_col = []
        for row in range (len(str2)):
            col.append(0)
            b_col.append(0)
        s.append(col) 
        backtrack.append(b_col)   
    
   
    for i in range (1, len(str1)):
        for j in range (1, len(str2)):
            # add penalty to insertion/deletion
            ver = s[i-1][j]+sigma
            hor = s[i][j-1]+sigma
            letter1 = letters.index(str1[i])
            letter2 = letters.index(str2[j])
            #find the score of the copmbination of letter in str1[i] and str2[j]
            score = SCORE[letter1][letter2]
            conv = int(score)
            diag = s[i-1][j-1] +conv
            # choose the max between the possible paths to take or 0 
            # (beginning of the local alignment)
            s[i][j] = max( diag, ver, hor, 0)
            # save the position of the biggest score (this saves the end position of the
            # best local alignment, because the score is the biggest)
            if (s[i][j] > global_max):
                global_max = s[i][j]
                start_c = i
                start_r = j
            # saves the direction of the path in the backtrack matrix
            # If the direction is horizontal = 1, vertical =2, diagonal =3
            if s[i][j] == ver:
                backtrack[i][j] = 2
            elif s[i][j] == hor:
                backtrack[i][j] = 1
            else :
                backtrack[i][j] = 3
            
 
     
    print(global_max)
    align1,align2='',''; #initial sequences

    i,j=start_c,start_r; #indices of path starting point for the local alignment with the biggest Score
    # iterate until the beginning of the local alignment was found
    while s[i][j]!=0:
        # add both letters if direction is diagonal
        if backtrack[i][j]==3:
            align1=align1+str1[i];
            align2=align2+str2[j];
            #move diagonaly
            i=i-1;
            j=j-1;
        # add - for second str, and a letter from str1 to output.
        #Update only i position, j stays the same, move vertically
        elif backtrack[i][j]==2:
            align2=align2+'-';
            align1=align1+str1[i]
            i=i-1;
            
        else :
        # move horizontally, update index j and add letter to str2
            align2=align2+str2[j];
            align1=align1+'-';
            j=j-1;
            
    # flip the answers to start from the beginning 
    align1=align1[::-1]; 
    align2=align2[::-1]; 
    print(align1)
    
    print(align2)
  


    

if __name__ == "__main__":
  main()