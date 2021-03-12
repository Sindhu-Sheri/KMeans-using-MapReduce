#!/usr/bin/python3

"""u_reducer.py"""

import json
import sys
from operator import add

dict_value = {}
dict_count = {}
dict_final_count = {}
for i in sys.stdin:
    cluster_label = json.loads(i)
    for label in cluster_label:
        tlist = [int(j) for j in label[1][1:]]
        if label[0] not in dict_value:
            dict_value[label[0]] = tlist
            dict_final_count[label[0]] = 1
            dict_count[label[0]] = {}
            if label[1][0] not in dict_count[label[0]]:
                dict_count[label[0]][label[1][0]] = 1
        else:
            dict_value[label[0]] = list(map(add, tlist,dict_value[label[0]]))
            dict_final_count[label[0]] = dict_final_count[label[0]]+1
            if label[1][0] not in dict_count[label[0]]:
                dict_count[label[0]][label[1][0]] = 1
            else:
                dict_count[label[0]][label[1][0]] = dict_count[label[0]][label[1][0]]+1
newcentroid = []
for i,j in dict_value.items():
    listA = [max(dict_count[i],key=dict_count[i].get)]
    listB = [round(j/dict_final_count[i],4) for j in dict_value[i]]
    newcentroid.append(listA+listB)
for i in newcentroid:
    print(*i,sep=",")
