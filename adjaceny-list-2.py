import collections
from typing import List


class Graph:
    def __init__(self) -> None:
        self.graph = collections.defaultdict(List)

    
    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)
    

    def print_graph(self):
        for node, adjacentNodes in self.graph.items():
            print(node + "->")
            for adjNode in adjacentNodes:
                print(node, end="")
            

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(0, 2)
graph.add_edge(3, 4)
graph.add_edge(1, 3)

    

