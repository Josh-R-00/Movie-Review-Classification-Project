import numpy as np

TrainData = open("../Features/updatedLabeledBowTrain.txt").read().splitlines()
TestData = open("../Features/updatedLabeledBowTest.txt").read().splitlines()
vocab = open("../aclImdb/imdb.vocab", errors='ignore').read().splitlines()

reviews = open("../Features/labeledBowTrain.txt").read().splitlines()

TrainFeatures = np.zeros((len(TrainData), len(vocab)))
TrainLabels = np.zeros(len(TrainData))
TestFeatures = np.zeros((len(TestData), len(vocab)))
TestLabels = np.zeros(len(TestData))

updatedReviews = ""

for i in range(0, len(TrainData)):
    bag = TrainData[i].split()
    TrainLabels[i] = int(bag.pop(0))
    for word in bag:
        pair = word.split(":")
        TrainFeatures[i][int(pair[0])] = float(pair[1])

for i in range(0, len(TestData)):
    bag = TestData[i].split()
    TestLabels[i] = int(bag.pop(0))
    for word in bag:
        pair = word.split(":")
        TestFeatures[i][int(pair[0])] = float(pair[1])

def getTrainFeatures():
    return TrainFeatures

def getTrainLabels():
    return TrainLabels

def getTestFeatures():
    return TestFeatures

def getTestLabels():
    return TestLabels
