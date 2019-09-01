import sys


class Node(object):

    def __init__(self, name, n):
        self.name = name
        self.number = n
        self.visited = False
        self.adjacenciesList = []
        self.neighbours = []
        #self.rows = self.columns = m
        #self.routingTable = [[99 for i in range(self.rows)] for j in range(self.columns)] #-----routing table of 3 columns(dest,cost,nextHop), increasing number of adjacent Nodes
        self.routingTable = []#----- Destination, Cost, Next Hop
        self.predecessor = None
        self.minDistance = sys.maxsize
