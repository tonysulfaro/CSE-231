import pylab

listOfInts = []
for counter in range(10):
    listOfInts.append(counter*2)

print(listOfInts)
print(len(listOfInts))

pylab.plot(listOfInts)
pylab.show()    #hay thats pretty neato