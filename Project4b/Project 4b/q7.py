import Testing

print "testXorData"
perceptrons = 0
while True:
    itrNum = 1
    accuracy = []
    while itrNum < 6:
        print "iteration number: # ", itrNum
        nnet, testAccuracy = Testing.buildNeuralNet(Testing.xorData, maxItr = 200, hiddenLayerList = [perceptrons])
        accuracy.append(testAccuracy)
        itrNum += 1
    print "Maximum: ", max(accuracy)
    print "Average: ", Testing.average(accuracy)
    print "Standard Deviation: ", Testing.stDeviation(accuracy)
    perceptrons += 1
    if Testing.average(accuracy) > 0.99:
        break