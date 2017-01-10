#!/usr/bin/python
import csv
from preprocessing import complete_preprocessing


file=open( "sample_set.csv", "r")
reader = csv.reader(file)
tagged = open('tagged_tweet.txt','w')
l = []
for line in reader:
    print line[0] + ' ' + line[5]
    print line[5] 
    l.append(line[0])
    l.append(complete_preprocessing(line[5]))
    tagged.write(str(l))
    tagged.write('\n')
    l=[]
tagged.close()
