#! /usr/bin/python
from collections import defaultdict
import secrets
import json

log = open("vote.log", "a")

DNN = ["etape", "90"]
RNN = ["cc", "70"]
HMM = ["echap", "30"]
GMM = ["hey", "80"]

#List all the duplicate element and their index
def list_duplicates(seq):
    tally = defaultdict(list)
    result = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    for key,locs in tally.items():
        if len(locs)>1:
            result[key].append(locs)
    return result

#Calculate number of elements
def ilen(src):
    return sum(1 for elmt in src)

def rand_idx(locs):
    nbr_locs = ilen(locs[0])
    rand_res = secrets.randbelow(nbr_locs)

    return rand_res

    
#Choose the good word from a list with his certitude. If there are the same cert, random between both, work for more than 4 lists
def noDupli(word,cert):
    dupli_cert = list_duplicates(cert)
    nbr_dupli_cert = ilen(dupli_cert)
    max_cert = max(cert)
    idx_max = cert.index(max_cert)

    if nbr_dupli_cert is 0:
        return word[idx_max]

    elif nbr_dupli_cert is 1:
        for key,locs in dupli_cert.items():
            if max_cert in key: #If the max certitude is the dupli
                rand_loc = rand_idx(locs)
                return word[locs[0][rand_loc]]
            else: #if the max certitude is not dupli
                return word[idx_max]

    else:
        for key,locs in dupli_cert.items():
            if max_cert is key:
                rand_loc = rand_idx(locs)
                return word[locs[0][rand_loc]]

#Determines duplicate value as the result
def oneDupli(dupli_list, word):
    for dupli in dupli_list:
        return(dupli)

#Determine between 2 words which is better, /!\ only work for 4 lists from ML
def eqDupli(cert,dupli_list,word):
    dupli_cert = list_duplicates(cert)
    nbr_dupli_cert = ilen(dupli_cert)
    max_cert = max(cert)
    idx_max = cert.index(max_cert)
    list_idx = []
    mean_w1 = 0
    mean_w2 = 0

    #Get all location by key in a list
    for key, locs in dupli_list.items():
        list_idx.append(locs[0])

    #mean of certitude of each words
    mean_w1 = (int(cert[list_idx[0][0]]) + int(cert[list_idx[0][1]]))/2
    mean_w2 = (int(cert[list_idx[1][0]]) + int(cert[list_idx[1][1]]))/2

    if mean_w1 > mean_w2:
        return word[list_idx[0][0]]
    elif mean_w2 > mean_w1:
        return word[list_idx[1][0]]
    elif mean_w1 == mean_w2: #if means are equals
        if nbr_dupli_cert is 0: #if there is no duplicated cert return the word with the max cert
            return word[idx_max]
        else: # else random between the 2 words
            rand_word = secrets.randbelow(2)
            if rand_word is 1:
                return word[list_idx[0][0]]
            else:
                return word[list_idx[1][0]]

def vote(*result_module):
    cert = []
    word = []

    for listNN in result_module:
        word.append(listNN[0])
        cert.append(listNN[1])
    
    json.dump(word, log)
    log.write("\n")
    json.dump(cert, log)
    log.write("\n")

    dupli_list = list_duplicates(word)
    nbr_dupli_word = ilen(dupli_list)

    if nbr_dupli_word is 0:
        return noDupli(word,cert)
    elif nbr_dupli_word is 1:
        return oneDupli(dupli_list,word)
    elif nbr_dupli_word is 2:
        return eqDupli(cert,dupli_list,word)

    return word

result_vote = vote(DNN,RNN,HMM,GMM)
log.write(result_vote + "\n\n")
print(result_vote)