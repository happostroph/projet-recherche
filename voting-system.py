#! /usr/bin/python
from collections import defaultdict
import secrets

DNN = ["etape", "90"]
RNN = ["cc", "80"]
HMM = ["echap", "90"]
GMM = ["patate", "80"]

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

    
#Choose the good word from a list with his certitude. If there are the same cert, random between both
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

    elif nbr_dupli_cert is 2:
        for key,locs in dupli_cert.items():
            if max_cert is key:
                rand_loc = rand_idx(locs)
                return word[locs[0][rand_loc]]

#Determines duplicate value as the result
def oneDupli(dupli_list, word):
    for dupli in dupli_list:
        return(dupli)

def eqDupli(cert,word):
    dupli_cert = list_duplicates(cert)

    for key,locs in dupli_cert.items():
        raise NotImplementedError
    #TODO : prendre la moyenne des deux dupli, si moyenne = prendre la certitude la plus haute
    

def vote(*result_module):
    cert = []
    word = []

    for listNN in result_module:
        word.append(listNN[0])
        cert.append(listNN[1])
    
    dupli_list = list_duplicates(word)
    nbr_dupli_word = ilen(dupli_list)

    if nbr_dupli_word is 0:
        print("tous diff")
        return noDupli(word,cert)
    elif nbr_dupli_word is 1:
        print("un mot dupli")
        return oneDupli(dupli_list,word)
    elif nbr_dupli_word is 2:
        print("NN has found 2 result possible")
        return eqDupli(cert,word)

    return word

result_vote = vote(DNN,RNN,HMM,GMM)
print(result_vote)