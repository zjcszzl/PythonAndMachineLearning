import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.edges = []

    def addEdge(self, target, weight):
        self.edges.append(Edge(self, target, weight))


class Edge:
    def __init__(self, from_, to_, weight):
        self.start = from_
        self.end = to_
        self.w = weight


class Graph:
    def __init__(self):
        # self.edges = dict()  # node to list of adges
        self.nodes = dict()  # value to node

    # add Node()
    def addNode(self, val):
        node = Node(val)
        self.nodes[val] = node

    # add Edge(from ,to)
    def addEdge(self, from_, to_, weight):
        if from_ not in self.nodes:
            print(from_ + " is not in Graph")
            return
        if to_ not in self.nodes:
            print(to_ + " is not in Graph")
            return
        from_node = self.nodes[from_]
        to_node = self.nodes[to_]
        from_node.addEdge(to_node, weight)
        to_node.addEdge(from_node, weight)

    def print_(self):
        for k, v in self.nodes.items():
            for elem in v.edges:
                print(elem.start.val, elem.end.val, elem.w)


if __name__ == "__main__":
    g = Graph()
    g.addNode("A")
    g.addNode("B")
    g.addNode("C")
    g.addEdge("A", "B", 3)
    g.addEdge("A", "C", 2)
    g.print_()
