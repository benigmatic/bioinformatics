# Find Frequent Words with Mismatches and Reverse Complements


neighborsCache = {}


def patternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count


def reverseComplement(text):
    reverse = ""
    for i in text:
        if i == 'A':
            reverse = "T" + reverse
        elif i == 'T':
            reverse = "A" + reverse
        elif i == 'G':
            reverse = "C" + reverse
        else:
            reverse = "G" + reverse
    return(reverse)


def getNeighbors(pattern, d):
    if pattern in neighborsCache:
        forPattern = neighborsCache[pattern]
        if not forPattern is None:
            if str(d) in forPattern:
                return forPattern[str(d)]
    return None


def setNeighbors(pattern, d, val):
    forPattern = {}
    if pattern in neighborsCache:
        forPattern = neighborsCache[pattern]
    forPattern[str(d)] = val
    neighborsCache[pattern] = forPattern


def Neighbors(pattern, d):

    cached = getNeighbors(pattern, d)
    if cached is not None:
        return cached
    neighbors = set([pattern])
    if (d == 0) or len(pattern) == 0:
        return neighbors
    alphabet = 'ATCG'
    for base in alphabet:
        if not (pattern[0] == base):
            suffixes = Neighbors(pattern[1:], d - 1)
        else:
            suffixes = Neighbors(pattern[1:], d)
        for suffix in suffixes:
            neighbors.add(base + suffix)
    setNeighbors(pattern, d, neighbors)
    return neighbors


def addCount(counts, pattern):
    if pattern in counts:
        counts[pattern] += 1
    else:
        counts[pattern] = 0
    return counts


def frequentWordsWithMismatches(text, k, d):
    counts = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        neighborhood = Neighbors(pattern, d)
        for neighbor in neighborhood:
            reverseNeighbor = reverseComplement(neighbor)
            counts = addCount(counts, reverseNeighbor)
            counts = addCount(counts, neighbor)
    freq = set()
    maxCount = None
    for pattern in counts:
        count = counts[pattern]
        if maxCount is None or count > maxCount:
            freq = set([pattern])
            maxCount = count
        elif count == maxCount:
            freq.add(pattern)
    return freq


def main():
    input = "".join(open('input.txt')).split()
    # read input
    text = input[0]
    k = int(input[1])
    d = int(input[2])

    frequentPatterns = frequentWordsWithMismatches(text, k, d)
    solution = " ".join(frequentPatterns)

    print(solution)


if __name__ == "__main__":
    main()
