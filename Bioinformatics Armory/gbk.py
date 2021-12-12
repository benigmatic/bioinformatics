#GenBank Introduction
from Bio import Entrez
input = "".join(open('input.txt')).splitlines()
genus = input[0]
date1 = input[1]
date2 = input[2]

Entrez.email = '152000alexandra@gmail.com'
handle = Entrez.esearch(db='nucleotide', term=genus+'[ORGN]', mindate=date1, maxdate=date2, datetype='pdat')
record = Entrez.read(handle)

print (record['Count'])
