import itertools


def CircularPath(k):
    kmers = perm(k)
    graph = debrujin(kmers)
    cycle = Eulerian(graph)
    
    cycle = cycle[:-(k-1)]
    genome = cycle[0][:-1]
    for i in cycle:
        genome += i[-1]
    return genome


def Eulerian(kmers):
    stack = []
    random_vertex = sorted(kmers.keys())[0]
    stack.append(random_vertex)
    path = []
    while stack != []:
        u_v = stack[-1]
        try:
            w = kmers[u_v][0]
            stack.append(w)
            kmers[u_v].remove(w)
        except:
            path.append(stack.pop())
    return path[::-1]


def perm(k):    
    kmers = ["".join(list(i)) for i in itertools.product(["0", "1"], repeat=k)]
    
    return sorted(kmers)


def debrujin(patterns):
    kmers = []
    for pattern in patterns:
        kmers = kmers+suffix_composition(len(pattern), pattern, uniq=True)
    kmers = set(kmers)
    dict = {}
    for kmer1 in kmers:
        dict[kmer1] = []
    for kmer in patterns:
        dict[prefix(kmer)].append(suffix(kmer))
    return dict


def suffix_composition(k, text, uniq=False):
    kmers = []
    for i in range(len(text)+1-k):
        kmers.append(text[i:i+k-1])
    if uniq:
        return sorted(list(kmers))
    else:
        return sorted(kmers)


def suffix(string):
    return string[1:]


def prefix(string):
    return string[0:-1]


if __name__ == "__main__":
    input = "".join(open('input.txt')).split()
    k = int(input[0])
    print(CircularPath(k))