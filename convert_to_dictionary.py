import csv

file = open("tagged_tweet.txt")
make_dictionary = {}
count = 5


for i in file:
    value = i[2]
    if value == 0:
        add = -.2
    elif value == 2:
        add = 0
    else:
        add = +.2 

    for j in  list(i[6:len(i)-2].split(",")):
        if j[0] == "[":
            j=j[1:]
        if j[len(j)-1]=="]":
	    j=j[:len(j)-1]
        j = j.replace("'","").strip(" ");
        if j in make_dictionary.keys():
            make_dictionary[j] = make_dictionary[i] + add           
        else:
           make_dictionary[j] = add
file.close()

w = csv.writer(open("dictionary.csv", "w"))
for key, val in make_dictionary.items():
    w.writerow([key, val])



print make_dictionary  	    
