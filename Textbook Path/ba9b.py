#Implement TrieMatching
def ConstructTrie(patterns):
    # trie with single node root
    trie = {}
    trie[0] = {}
    node = 1
    root = 0
    # for each pattern in patterns
    for i in range(len(patterns)):
        pattern = patterns[i]
        # add ending $ for the pattern
        pattern = pattern + "$"
        # current Node = root
        currentNode = root
        for j in range(len(pattern)):
            # current symbol = ith symbol of patterns
            currentSymbol = pattern[j]
            # there is an ongoing edge from CurrentNode with label currentSymbol
            if currentSymbol in trie[currentNode]:
                currentSymbol = trie[currentNode][currentSymbol]
            else:
                # add new node to the trie
                trie[node] = {}
                # add a new edge
                trie[currentNode][currentSymbol] = node
                # switch to the new node
                currentNode = node
                node += 1
    return trie


def prefixTrieMatching(text, trie):
    # symbol is the first letter of text
    symbol = text[0]

    w = 0
    l = len(text)
    # v is root of Trie
    v = 0
    while True:
        # if v is a leaf in Trie
        if "$" in trie[v]:
            return 1
        # if there is an edge v,w in trie  labeled by symbol
        elif symbol in trie[v]:

            v = trie[v][symbol]
            # if we are not in the end of text, move to the next symbol
            if w < l - 1:
                w += 1
                # symbol is the next letter of text
                symbol = text[w]

        else:
            # print("no matches found")
            return -1


def trieMatching(text, trie):
    result = []
    for i in range(len(text)):
        if prefixTrieMatching(text[i:], trie) != -1:
            result.append(i)

    return result


def main():
    input = "".join(open("input.txt")).split()
    # read input
    text = input[0]
    patterns = input[1:]
    trie = ConstructTrie(patterns)
    result = trieMatching(text, trie)
    print(*result)


if __name__ == "__main__":
    main()
