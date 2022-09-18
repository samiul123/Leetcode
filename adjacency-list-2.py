import collections


class Graph:
    def __init__(self) -> None:
        self.graph = collections.defaultdict(list)
    

    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))
    

    def print_graph(self):
        for node, adjNodes in self.graph.items():
            print(str(node) + " -> ", end="")
            for adjNode in adjNodes:
                print(str(adjNode) + " ", end="")
            print()


graph = Graph()
graph.add_edge(0, 1, 1)
graph.add_edge(0, 2, 2)
graph.add_edge(0, 3, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(2, 4, 2)
graph.add_edge(4, 1, 3)
graph.print_graph()
