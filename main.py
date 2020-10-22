import networkx as nx
import os
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
