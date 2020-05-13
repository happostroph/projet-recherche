#! /usr/bin/python
from collections import defaultdict
import secrets

DNN = ["etape", "90"]
RNN = ["cc", "70"]
HMM = ["echap", "80"]
GMM = ["patate", "50"]

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

#Choose the good word from a list with his certitude. If there are the same cert, random between both
def noDupli(word,cert):
    dupli_cert = list_duplicates(cert)
    nbr_dupli_cert = ilen(dupli_cert)

    if nbr_dupli_cert is 0:
        idx = cert.index(max(cert))
        return word[idx]
    elif nbr_dupli_cert is 1:
        #TODO : si certitude dupli, random entre les certitude similaire
        raise NotImplementedError
    elif nbr_dupli_cert is 2:
        #TODO : si 2 certitude différente en double prendre la plus haute et random
        raise NotImplementedError

#Determines duplicate value as the result
def oneDupli(dupli_list, word):
    for dupli in dupli_list:
        return(dupli)

def eqDupli(dupli_list,word):
    #TODO : prendre la moyenne des deux dupli, si moyenne = prendre la certitude la plus haute
    raise NotImplementedError

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
    

    return word

result_vote = vote(DNN,RNN,HMM,GMM)
print(result_vote)