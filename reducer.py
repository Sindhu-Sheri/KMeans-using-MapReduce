#!/usr/bin/python3

#This reducer function averages the features of all data instances in a particular cluster
#This Function takes cluster_label list as argument returned by mapper function
#Returns a list of newly generated centroids
"""reducer.py"""

#importing the required libraries
import json
import sys
from operator import add

#dictionary which has the sum of co-ordinates of a particular cluster
dict_value = {}
#dictionary to store the count of elements in a cluster
dict_final_count = {}

for i in sys.stdin:
    #de-serializing the python object returned by mapper
    cluster_label = json.loads(i)
    #iterating the list returned from mapper
    for label in cluster_label:
        #get the co-ordinates of each data point
        tlist = [int(j) for j in label[1][1:]]
        #building the dictionary 
        if label[0] not in dict_value:
            dict_value[label[0]] = tlist
            dict_final_count[label[0]] = 1
        else:
            dict_value[label[0]] = list(map(add, tlist,dict_value[label[0]]))
            dict_final_count[label[0]] = dict_final_count[label[0]]+1
#newcentroid is a list which stores new centroids
newcentroid = []
for i,j in dict_value.items():
    listA = [i]
    #calculating the co-ordinates of new centroids
    listB = [round(j/dict_final_count[i],4) for j in dict_value[i]]
    newcentroid.append(listA+listB)
#returing the newcentriods list elements as comma separted values
for i in newcentroid:
    print(*i,sep=",")
