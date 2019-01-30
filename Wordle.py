import re 
import operator


def wordcount() :
    
    f = open("wordcount.txt", "r")
    #print(f.read().lower())
    wordle = f.read().lower()
    
    whitelist = set('abcdefghijklmnopqrstuvwxyz \n')
   
    
    wordle = ''.join(filter(whitelist.__contains__, wordle))
    wordlist = wordle.split()
    #print (wordlist)
    
    wordCount = {}
    blacklist = ('and','the', 'to', 'of', 'our' )
    
    for word in wordlist:
        #print (word)
        if word in blacklist:
            continue
            
        if word in wordCount:
            wordCount[word] += 1    
        else:
            wordCount[word]=1
            
    #print (wordCount)
    
    sorted_WC = sorted(wordCount.items(), key=operator.itemgetter(1))
    for row in sorted_WC:
        print ("%s,%s" % (row[0] , row[1]) )
        