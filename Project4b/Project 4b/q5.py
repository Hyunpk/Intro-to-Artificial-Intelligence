import Testing

print "testPenData"
itrNum = 1
accuracy = []
while itrNum < 6:
    print "iteration number: # ", itrNum
    nnet, testAccuracy = Testing.testPenData()
    print "accuracy: ", testAccuracy
    accuracy.append(testAccuracy)
    itrNum += 1
print "Maximum: ", max(accuracy)
print "Average: ", Testing.average(accuracy)
print "Standard Deviation: ", Testing.stDeviation(accuracy)

print "testCarData"
itrNum = 1
accuracy = []
while itrNum < 6:
    print "iteration number: # ", itrNum
    nnet, testAccuracy = Testing.testCarData()
    print "accuracy: ", testAccuracy
    accuracy.append(testAccuracy)
    itrNum += 1
print "Maximum: ", max(accuracy)
print "Average: ", Testing.average(accuracy)
print "Standard Deviation: ", Testing.stDeviation(accuracy)
