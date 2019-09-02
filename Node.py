import sys


class Node(object):

    def __init__(self, name, n):
        self.name = name
        self.number = n
        self.neighbours = []
        self.routingTable = []#----- Destination, Cost, Next Hop
