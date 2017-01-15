from preprocessing import complete_preprocessing


with open("dictionary.csv", "r") as ins:
    dictionary = {}
    for line in ins:
        line = line.split(",")
        dictionary[line[0]] = line[1][:-2]

print dictionary

tweet = "hii test tweet bounds"
tweet = complete_preprocessing(tweet)
print tweet

pos = 1
neg = 1

for i in tweet:
    if i in dictionary.keys():
        if dictionary[i] > 0:
            pos = pos + float(dictionary[i])
        else:
	    neg = neg + float(dictionary[i])

print pos
print neg


