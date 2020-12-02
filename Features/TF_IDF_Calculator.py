import math

docFreq = open("wordDocFreqTrain.txt", errors='ignore').read().splitlines()

def TF_score(pair):
    left = int(pair[0])
    right = int(pair[1])
    return right * math.log(25000/int(docFreq[left]))

reviews = open("labeledBowTrain.txt").read().splitlines()

updatedReviews = ""

for line in reviews:
    bag = line.split()
    updateLine = bag.pop(0) + " "
    for word in bag:
        pair = word.split(":")
        updateLine += pair[0]
        updateLine += ":"
        updateLine += str(TF_score(pair))
        updateLine += " "
    updateLine += "\n"
    updatedReviews += updateLine

with open('updatedLabeledBowTrain.txt', 'w') as file:
    file.write("%s" % updatedReviews)