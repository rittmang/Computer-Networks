import numpy as np
from Algorithm import *
from Node import *
from Edge import *

vertexList = []
edgeList = []
print("Enter number of routers:")
n = int(input())
for i in range(n):
    print("Enter label for router %d " % i)
    node = Node(input(), i, n)#sends n for routing table setup (i.e number of rows and columns to be set up)
    vertexList.append(node)

print("Initiating....")

#-------------------Routers set up

print("Enter number of links:")
m = int(input())
for i in range(m):
    print("Source Name, Destination Name, Cost:")
    sourceLabel = Node(input(), 0, 0)
    destLabel = Node(input(),0, 0)#don't make another routing table, since will be replaced
    cost = int(input())

    for i in vertexList:
        if i.name == sourceLabel.name:
            sourceLabel = i
        if i.name == destLabel.name:
            destLabel = i

    edge = Edge(cost,sourceLabel,destLabel)
    if edge not in sourceLabel.adjacenciesList:
        sourceLabel.adjacenciesList.append(edge)
        ind = sourceLabel.number


    if edge not in destLabel.adjacenciesList:
        destLabel.adjacenciesList.append(edge)

    ind1 = sourceLabel.number
    ind2 = destLabel.number

    sourceLabel.routingTable[ind2][ind2] = cost
    destLabel.routingTable[ind1][ind1] = cost
    edgeList.append(edge)

print("-----------------INITIALIZATION------------------------")
for i in vertexList:
    print(i.name,"'s Routing Table:")
    for j in i.routingTable:
        for k in j:
            print(k,"\t",end='')
        print()
    print()


# print("Select start node:")
# node_start = Node(input())
# for i in vertexList:
#     if i.name == node_start.name:
#         node_start = i
#
# print("Select end node:")
# node_end = Node(input())
# for i in vertexList:
#     if i.name == node_end.name:
#         node_end = i
#
# # edge1 = Edge(1, node1, node2)
# # edge2 = Edge(1, node2, node3)
# # edge3 = Edge(1, node3, node4)
# # edge4 = Edge(4, node3, node2)
# # edge5 = Edge(300, node1, node4)
# #
# # node1.adjacenciesList.append(edge1)
# # node1.adjacenciesList.append(edge2)
# # node2.adjacenciesList.append(edge3)
# # node3.adjacenciesList.append(edge4)
# # node3.adjacenciesList.append(edge2)
#
# #vertexList = [node1, node2, node3, node4]
# # edgeList = [edge1, edge2, edge3, edge4, edge5]
#
# algorithm = Algorithm()
# algorithm.calculateShortestPath(vertexList, edgeList, node_start)
# algorithm.getShortestPath(node_end)
