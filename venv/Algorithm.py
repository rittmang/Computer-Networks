class Algorithm(object):
    HAS_CYCLE = False

    def shareRT(self, vertexList):
        for receiver in vertexList:
            for sender in vertexList:
                if sender.name != receiver.name:
                    print("Ensure router does not send itself, its routing table")



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
