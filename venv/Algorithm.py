class Algorithm(object):
    HAS_CYCLE = False

    def myFunc(e):
        return e

    @staticmethod
    def shareRT(vertexList):

        print("Routing Tables being transmitted 1 by 1:")
        #UPDATE_HAPPENED = False

        while True:
            UPDATE_HAPPENED = False
            for receiver in vertexList:
                print("-----------------------------------------------")
                for sender in receiver.neighbours:
                    current_cost = 0
                    for lol in receiver.routingTable:
                        if lol[0] == sender.name:
                            current_cost = lol[1]
                    print(sender.name," sends its DV to ",receiver.name," , and is at distance ",current_cost," from it.")

                    for i in receiver.routingTable:
                        L1 = list(i)
                        for j in sender.routingTable:
                            L2 = list(j)
                            if (i[0] == j[0]) & ((j[1] + current_cost) < i[1]):
                                print(L1, "\t", " and ",end='')
                                print(L2, " ",end='')
                                L1[1] = L2[1]+current_cost
                                L1[2] = sender.name
                                receiver.routingTable.remove((i[0],i[1],i[2]))
                                i = tuple(L1)
                                receiver.routingTable.append(i)
                                print(" updates L1 to ",i)
                                UPDATE_HAPPENED = True
                            else:
                                continue
                        #i = tuple(L1)

                print("-----------------UPDATION------------------------")
                print(receiver.name, "'s Routing Table:")
                receiver.routingTable.sort()
                for j in receiver.routingTable:
                    print(j, "\t", end='')
                print()

            if(UPDATE_HAPPENED == False):
                break

        print("STABLE STATE REACHED!")

    def calculateShortestPath(self, vertexList, edgeList, startVertex):
        startVertex.minDistance = 0

        for i in range(0, len(vertexList) - 1):
            for edge in edgeList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u

        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative cycle detected")
                Algorithm.HAS_CYCLE = True
                return

    @staticmethod
    def hasCycle(edge):
        if (edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
            return True
        else:
            return False

    @staticmethod
    def getShortestPath(targetVertex):
        if not Algorithm.HAS_CYCLE:
            print("Shortest path to targetVertex: ", targetVertex.minDistance)
            node = targetVertex

            while node is not None:
                print("%s -> " % node.name)
                node = node.predecessor
