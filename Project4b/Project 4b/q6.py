import Testing

print "testPenData"
perceptrons = 0
while perceptrons < 41:
    itrNum = 1
    accuracy = []
    while itrNum < 6:
        print "iteration number: # ", itrNum
        nnet, testAccuracy = Testing.buildNeuralNet(Testing.penData, maxItr = 100, hiddenLayerList = [perceptrons])
        accuracy.append(testAccuracy)
        itrNum += 1
    print "Maximum: ", max(accuracy)
    print "Average: ", Testing.average(accuracy)
    print "Standard Deviation: ", Testing.stDeviation(accuracy)
    perceptrons += 5

print "testCarData"
perceptrons = 0
while perceptrons < 41:
    itrNum = 1
    accuracy = []
    while itrNum < 6:
        print "iteration number: # ", itrNum
        nnet, testAccuracy = Testing.buildNeuralNet(Testing.carData, maxItr = 100, hiddenLayerList= [perceptrons])
        accuracy.append(testAccuracy)
        itrNum += 1
    print "Maximum: ", max(accuracy)
    print "Average: ", Testing.average(accuracy)
    print "Standard Deviation: ", Testing.stDeviation(accuracy)
    perceptrons += 5
