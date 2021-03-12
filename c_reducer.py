#!/usr/bin/python3

"""c_reducer.py"""

import json
import sys
from operator import add

dict_freq_count = {}
for i in sys.stdin:
    cluster_label = json.loads(i)
    for label in cluster_label:
      if label[1][0] not in dict_freq_count:
          dict_freq_count[label[1]] = list(label[0])
      else:
          dict_freq_count[label[1]].append(label[0])
finalList = []
for i,j in dict_freq_count.items():
    listA = [i]
    listB = (sorted(j))
    finalList.append(listA+listB)
for x in finalList:
    print(*x,sep=",")
