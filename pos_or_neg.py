from preprocessing import complete_preprocessing


with open("dictionary1.csv", "r") as ins:
    dictionary = {}
    for line in ins:
        line = line.split(",")
        dictionary[line[0]] = line[1][:-2]

#print dictionary

tweet = raw_input("enter the tweet - ") 
tweet = complete_preprocessing(tweet)
print tweet

pos = 1
neg = 1
sign = 1

for i in tweet:
	if i == "not":
		sign = -1
        else:

	    if i in dictionary.keys(): 
	        value = (sign * float(dictionary[i]))*10
	        if value > 0:
	            pos = pos + value
	        else:
	            neg = neg - value
	    sign = 1        

print "pos " + str(pos)
print "neg " + str(neg)

diff = float(pos - neg)
print "diff " + str(diff)
divide = pos + neg
print "divide "+ str(divide)
per = (diff / divide)*50
print "per " +str(per)

per = 50 + per
print str(per) + "%"
