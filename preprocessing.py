import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
from collections import Counter
from spell_correction import correction 
ps = PorterStemmer()

def preprocessing(tweet):
    #convrt into lower case 
    tweet = tweet.lower()
    #convert @title to AT_USER
    tweet = re.sub("@[^\s]+","",tweet)
    #convert #hashtag into hashtag
    tweet = re.sub('#',"",tweet)
    #convert url to "URL"
    tweet = re.sub('((www\.[^s\]+)|(https?://[^s]+))','',tweet)
    #convert multiple space into single space
    tweet = re.sub('[\s]+', ' ' ,tweet)
    #convert ! into ""
    tweet = re.sub("!","",tweet)
    #trim
    tweet = tweet.strip(" ")  
    #remove dot
    tweet = re.sub('[\.]+','',tweet)
       
    return tweet


def nltk_preprocessing(tweet):
    stop_words = list(stopwords.words("english"))
    #stop_words.append('AT_USER')
    #stop_words.append('URL')
    #print stop_words
    words = word_tokenize(tweet)
    filtered_sentence = []
    #print stop_words
    for w in words:
    	if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence


def remove_length_one_word(tweet):
    l = []
    for i in tweet:
        if len(i) >= 2:
            l.append(i)	
    return l

def remove_word_starting_with_number(tweet):
    l = []
    for i in tweet:    
        if not  (re.match('^[0-9][^\s]+',i)):
            l.append(i)
    return l

def word_correct(tweet):
    l = [] 
    for i in tweet:
        l.append(correction(i))
    return l



#tweet = "@PrincessSuperC Hey Cici #sweetheart! Just wanted to let u know I luv u! OH! and will the mixtape drop soon? FANTASY RIDE MAY 5TH!!!!"

def complete_preprocessing(tweet):
    tweet = preprocessing(tweet)
    tweet = nltk_preprocessing(tweet)
    tweet = remove_length_one_word(tweet)
    tweet = remove_word_starting_with_number(tweet)
    tweet = word_correct(tweet)
    return tweet



