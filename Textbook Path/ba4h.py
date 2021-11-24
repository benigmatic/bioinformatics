
#Generate the Convolution of a Spectrum
import operator

def spectral_convolution(spectrum):
    spectrum.sort()
    result = {}
    res = []
    for i in range(len(spectrum) - 1):
        for j in range(i, len(spectrum)):
            if spectrum[j] > spectrum[i]:
                result[spectrum[j]-spectrum[i]] = result.get(spectrum[j] - spectrum[i], 0) + 1
    
    keys = list(result.keys())
    vals = list(result.values())
    
    for i in range(len(vals)):
        for j in range(vals[i]):
            res.append(keys[i])
    return res


if __name__ == "__main__":
    input = "".join(open('input.txt')).split()
    spectrum = input[0:]
    spectrum = [int(spectrum[i]) for i in range(len(spectrum))]
    res = spectral_convolution(spectrum)
    print(*res)
    with open("output.txt", "w") as external_file:
       
        for i in (res):
            print(i,end=" ",file=external_file)
        external_file.close()

