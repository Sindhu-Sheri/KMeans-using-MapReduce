#!/usr/bin/python3

#This mapper function calculates the distance from each datapoint & each centroid, assigns the data instance with new centroid whose distance is minimum
#This function takes train data list & centroids data list as arguments
#This function returns a clusterlabel(list of lists) where each list has original data instance label & newly assigned centroid label 
#['N','T]
"""c_mapper.py"""

#importing libraries
import sys
import pickle
import json

#List to store centroids data
centroidList = []
f = open('centroids.txt', 'r')
for line in f:
    if line != []:
        centroidList.append(line.strip().split(","))

#Function to calculate eucledian distance b/w a datapoint & centroid
#This function takes two lists a(data point),b(Centroid) as arguments
def compute_euclidean_distance(a,b):
    sum_of = 0
    #start from 1 as each data instance has a alphabet followed by 16 features
    for i in range(1,len(a)):
        ans = (float(a[i]) - float(b[i]))**2
        sum_of += ans
    return (sum_of)**(1/2)

#Function to assign the centroid to the data point which has the minimum distance
#This Function takes distance(dictionary with key,values as centroids,distance from centroid), datapoint(a particular data instance) & centroids list
def assign_label_cluster(distance, data_point, centroids):
    #getting the minimum distance centroid from the distance dictionary
    minIndex = min(distance, key=distance.get)
    return [centroids[minIndex][0], data_point[0]]

#List of lists which has to be returned
cluster_label = []
#iterating the datapoints
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split('\n')
    word = []
    for i in words:
        word = i.split(",")
    #dictionary to store corresponding distances between k centroids and current data point
    distance = {}
    #computing the distances for each centroid
    for c in range(0,len(centroidList)):
        distance[c] = compute_euclidean_distance(word, centroidList[c])
    #assigning the cluster to a smallest distance
    label = assign_label_cluster(distance, word, centroidList)
    cluster_label.append(label)
#returning the output as an json object(serialization in python)
print(json.dumps(cluster_label))
