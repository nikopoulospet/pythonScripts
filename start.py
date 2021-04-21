#!/usr/bin/python
import random

class Nodes:
    def __init__(self):
        self.location = (-1,-1)
        self.searched = False
        self.neighbors = []
    
    def create(self, location, neighbors):
        self.location = location
        self.neighbors = neighbors
    
    def assign_neigbors(self, size):
        if self.location[0] + 1 in range(size[0]):
            self.neighbors.append(((self.location[0] + 1, self.location[1]),random.random()))
        if self.location[0] - 1 in range(size[0]):
            self.neighbors.append(((self.location[0] - 1, self.location[1]),random.random()))
        if self.location[1] + 1 in range(size[1]):
            self.neighbors.append(((self.location[0], self.location[1] + 1),random.random()))
        if self.location[1] - 1 in range(size[1]):
            self.neighbors.append(((self.location[0], self.location[1] - 1),random.random()))

    def set_searched(self):
        self.searched = True

    def set_unsearched(self):
        self.searched = False

class Map:
    def __init__(self):
        self.size = (10,10)
    
    def create_map(self):
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                node = Nodes()
                node.create((x,y), [])
                node.assign_neigbors(self.size)
                print node.neighbors 

if __name__ == "__main__":
    