# given a path , spells out the string by agenime path
def createGenome(path):
    result = ""
    result = result + path[0]
    n = len(path)-1
    for i in range(n):
        temp = path[i+1]
        result = result + temp[-1]
    return result
# creates the path based on the graph
def eulerianPath(Graph):
    path  = []
    #Get the first Node
    start = findFirstNode(Graph)
    #Assign the first "left" node as current
    cur = start
    flag =1

    while flag:
        #traverse through the graph    
        if cur in Graph and len(Graph[cur])!=0:            
            path.append(cur)   
            # select new "right" node (the first connection on the current node)         
            newCur = Graph[cur][0]
            # remove the "rigth" edge from graph
            Graph[cur].remove(newCur)
            # select the selected "right" node as the new "left" node
            cur = newCur
        elif cur in Graph and len(Graph[cur])==0:
            # base case we are at the last Node
            # We are at the last node, append it to the path
            path.append(cur)
            break
   # Create a string from the path created in the graph
    genome = createGenome(path)
    return genome
# finds the node which is located in the beginning of the graph
def findFirstNode(Graph):
    node = ""
    keys = Graph.keys()
    #Copy the keys for the the count set
    counts = {};
    counts = dict.fromkeys(keys);
    # set count to zero for all keys
    for i in Graph.keys():
        counts[i] =0
    # Each "left" node is decreased by one, each "right" node id increased. 
    # for the Nodes AT=== atg ==== TG, AT decreased by one, TG is increased by one
    # In the end we left out with first Node, with value -1. (The last node of the graph is +1)
    for prefix in Graph.keys():
        for suffix in Graph[prefix]:
            
            counts[prefix] -=1                  
            counts[suffix]+=1
    # search for the first node, it would have the count value of -1, that means that no prefix exists for this node   
    for i in counts.keys(): 
        if (counts[i]==-1):
            node = i
              
    return node
# Create a graph based on the kmers given
def Graph (kmers):
    result = {}
    n = len(kmers)
    for i in range(n):
        # get the prefix of the current k-mer
        prefix = kmers[i][1:] 
        
        #create a list for the prefix       
        result[prefix] = []
        for j in range (n):
            if i !=j:  
                #for all other k-mers but the selected find suffix and prefix   
                suffix = kmers[j][:-1]              
                                  
                if prefix == suffix:     
                    #if suffix of kmer[j]matches the  prefix of kmer[i] "connect" them             
                    node = kmers[j][1:]
                    result[prefix].append(node)
                   
    return result
def RecontructString(kmers):
    # Create a graph
    graph = Graph(kmers)
    #Create an eulerian Path
    genome = eulerianPath(graph)
    # prit the string spelled by a genome path
    print(genome)
    


def main():
    input = "".join(open('input.txt')).split()
    # read input
    k = int(input[0])
       
    kmers = input[1:]
    RecontructString(kmers)



if __name__ == "__main__":
  main()
