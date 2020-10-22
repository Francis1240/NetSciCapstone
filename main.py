import matplotlib.pyplot as plt
import math
import csv
import networkx as nx
import os
from scipy.optimize import curve_fit
GSeq = nx.MultiDiGraph()
GSen = nx.MultiGraph()
try:
    os.remove("seq.gexf")
except OSError:
    pass

try:
    os.remove("sen.gexf")
except OSError:
    pass

news_file = open("news.txt", "r", encoding="utf-8")
news_lines = news_file.readlines()

for line in news_lines:
    pre = '\0'
    for char in line:
        if pre != '\0' and char != '\n':
            GSeq.add_edge(pre, char)
        pre = char

nx.write_gexf(GSeq, "seq.gexf", encoding='utf-8')

for line in news_lines:
    for char1 in line:
        for char2 in line:
            if char1 != '\n' and char2 != '\n':
                GSen.add_edge(char1, char2)

nx.write_gexf(GSen, "sen.gexf", encoding='utf-8')

news_file.close()

with open('sen.csv', "r", newline='', encoding='utf-8') as sen_file:
    reader = csv.reader(sen_file, delimiter=',', quotechar='|')
    count = {0: 0}
    x = []
    y = []
    for row in reader:
        deg = math.floor(float(row[5]))
        count[deg] = count.get(deg, 0) + 1
    for k in count:
        x.append(k)
        y.append(count[k])

    plt.scatter(x, y, color="blue")
    plt.xscale("log")
    plt.yscale("log")
    plt.ylim(1, 40)
    plt.xlim(1, 13000)
    plt.title("Sentence Network")
    plt.xlabel("Weighted Degree")
    plt.ylabel("Count")
    plt.show()

with open('seq.csv', "r", newline='', encoding='utf-8') as seq_file:
    reader = csv.reader(seq_file, delimiter=',', quotechar='|')
    count = {0: 0}
    x = []
    y = []
    for row in reader:
        deg = math.floor(float(row[10]))
        count[deg] = count.get(deg, 0) + 1
    for k in count:
        x.append(k)
        y.append(count[k])

    plt.scatter(x, y, color="blue")
    plt.xscale("log")
    plt.yscale("log")
    plt.ylim(1, 500)
    plt.xlim(1, 1000)
    plt.title("Sequential Network")
    plt.xlabel("Weighted Degree")
    plt.ylabel("Count")
    plt.show()
