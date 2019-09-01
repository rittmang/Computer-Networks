import numpy as np
from Algorithm import *
from Node import *
from Edge import *
def myFunc(e):
    return e

vertexList = []
edgeList = []
print("Enter number of routers:")
n = int(input())
for i in range(n):
    print("Enter label for router %d " % i)
    node = Node(input(), i)#
    vertexList.append(node)
    node.routingTable.append((node.name, 0, node.name))

for router in vertexList:
    for other in vertexList:
        if other.name != router.name:
            router.routingTable.append((other.name, 99, other.name))


print("Initiating....")

#-------------------Routers set up

print("Enter number of links:")
m = int(input())
for i in range(m):
    print("Source Name, Destination Name, Cost:")
    sourceLabel = Node(input(), 0)
    destLabel = Node(input(),0)#don't make another routing table, since will be replaced
    cost = int(input())

    for i in vertexList:
        if i.name == sourceLabel.name:
            sourceLabel = i
        if i.name == destLabel.name:
            destLabel = i

    if destLabel not in sourceLabel.neighbours:
        sourceLabel.neighbours.append(destLabel)
    if sourceLabel not in destLabel.neighbours:
        destLabel.neighbours.append(sourceLabel)

    sourceLabel.routingTable.remove((destLabel.name, 99, destLabel.name))
    sourceLabel.routingTable.append((destLabel.name, cost, destLabel.name))
    destLabel.routingTable.remove((sourceLabel.name, 99, sourceLabel.name))
    destLabel.routingTable.append((sourceLabel.name, cost, sourceLabel.name))


print("-----------------INITIALIZATION------------------------")
for i in vertexList:
    print(i.name,"'s Routing Table:")
    i.routingTable.sort(key=myFunc)
    for j in i.routingTable:
          print(j,"\t",end='')
    print()


algorithm = Algorithm()
algorithm.shareRT(vertexList)


