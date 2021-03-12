#!/bin/bash
for (( i=1; i<=15; i++))
do
        hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -mapper "python3 /home/sisheri/sampleAssign/mapper.py" -reducer "python3 /home/sisheri/sampleAssign/reducer.py" -input /user/sisheri/Assign2Input/Train_40/Train/ -output /user/sisheri/sampleOutput -file /home/sisheri/sampleAssign/centroids.txt
        rm /home/sisheri/sampleAssign/centroids.txt
        hadoop fs -copyToLocal /user/sisheri/sampleOutput/part-00000 /home/sisheri/sampleAssign/centroids.txt
        hdfs dfs -rm /user/sisheri/sampleOutput/_SUCCESS
        hdfs dfs -rm /user/sisheri/sampleOutput/part-00000
        hdfs dfs -rmdir /user/sisheri/sampleOutput/
done
