import string

vocab = open("../aclImdb/imdb.vocab", errors='ignore').read().splitlines()
reviews = open("labeledBowTest.txt").read().splitlines()
docFreq = [0] * len(vocab)

for line in reviews:
    bag = line.split()
    bag.pop(0)
    for word in bag:
        pair = word.split(":")
        docFreq[int(pair[0])] += 1
        
with open('wordDocFreqTest.txt', 'w') as file:
    for word in docFreq:
        file.write("%s\n" % word)