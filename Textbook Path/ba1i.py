#Find the Most Frequent Words with Mismachtes in a String
def HammingDistance(str1, str2):
    count = 0
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            count += 1
    return(count)
def main():
    # reads input from terminal
    input = "".join(open('input.txt')).split()
    text = input[0]
    k = input[1]
    k = int(k)
    d = input[2]
    d = int(d)
    
    counts ={}
    for i in range(0, len(text) - k + 1 ):
	    kmer = text[i:i + k]
	    if kmer in counts:
		    counts[kmer] += 1
	    else:
		    counts[kmer] = 1

    updateCounts = {}

    for a in counts:
	    c = 0
	    for b in counts:
                dist = HammingDistance(a,b)
                
                if (dist<=d):
                    c+= counts.get(b)
	    
	    updateCounts[a] = c

    

    frequent = max(updateCounts.values())
    print(frequent)
    print()
    print(updateCounts)
    ans = []
    for k in updateCounts:
	    if updateCounts[k] == frequent:
		    ans.append(k)
    print(*ans)


if __name__ == "__main__":
  main()
