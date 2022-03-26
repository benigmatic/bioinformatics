# Read Quality Distribution
import statistics
from Bio import SeqIO
from statistics import mean
import os
import math
import pylab as plt
import numpy as np
import pandas as pd
import matplotlib.patches as patches



def plot_fastq_qualities(filename, ax=None, limit=10000):
    c = 0
    with open(filename, "r") as f:
        threshold = int(f.readline())
        scores = []
        for record in SeqIO.parse(f, "fastq"):
            quality = record.letter_annotations["phred_quality"]
            scores.append(quality)
    for i in range(len(scores[0])):
        if sum([q[i] for q in scores])/len(scores) < threshold:
            c += 1
    return c


c = plot_fastq_qualities("input.fastq")
print(c)