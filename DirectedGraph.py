import collections


class Node:
    def __init__(self, v):
        self.val = v
        self.next = None


class Graph:
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()

    # add Node()
    def addNode(self, val):
        node = Node(val)
        self.nodes[val] = node
        self.edges[node] = []

    # remove Node()
    def removeNode(self, val):
        if val not in self.nodes:
            print(val + " is not in Graph")
            return
        cur = self.nodes[val]
        for k, v in self.edges.items():
            if cur == k:
                self.edges.pop(k)
            elif cur in v:
                v.remove(cur)
        self.nodes.pop(val)

    # add Edge(from ,to)
    def addEdge(self, from_, to_):
        if from_ not in self.nodes:
            print(from_ + " is not in Graph")
            return
        if to_ not in self.nodes:
            print(to_ + " is not in Graph")
            return
        from_node = self.nodes[from_]
        to_node = self.nodes[to_]
        self.edges[from_node].append(to_node)
        # self.edges[to_node].append(from_node)

    # removeEdge(from to)
    def removeEdge(self, from_, to_):
        if from_ not in self.nodes:
            print(from_ + " is not in Graph")
            return
        if to_ not in self.nodes:
            print(to_ + " is not in Graph")
            return
        from_node = self.nodes[from_]
        to_node = self.nodes[to_]
        self.edges[from_node].remove(to_node)

    # print()
    def print_(self):
        for k, v in self.edges.items():
            if v:
                for child in v:
                    print(k.val, child.val)

    # BFS travsersal
    def BFS(self, val):
        res = ""
        if val not in self.nodes:
            return res
        cur = self.nodes[val]
        queue = collections.deque()
        queue.append(cur)
        seen = set()
        while queue:
            cur = queue.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            for child in self.edges[cur]:
                queue.append(child)
            res += cur.val
        return res

    # DFS travsersal
    def DFS(self, val):
        res = ""
        if val not in self.nodes:
            return res
        cur = self.nodes[val]
        stack = []
        stack.append(cur)
        seen = set()
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            for child in self.edges[cur]:
                stack.append(child)
            res += cur.val
        return res

    # Topological Sort
    def toplogicalSort(self):
        seen = set()
        l = []

        def helper(cur, seen, l):
            if cur in seen:
                return
            seen.add(cur)
            for child in self.edges[cur]:
                helper(child, seen, l)
            l.append(cur.val)

        for child in self.edges:
            helper(child, seen, l)
        return l


if __name__ == "__main__":
    g = Graph()
    g.addNode("A")
    g.addNode("B")
    g.addEdge("A", "B")
    g.addNode("C")
    g.addEdge("C", "A")
    g.addNode("D")
    g.addNode("E")
    g.addEdge("D", "E")
    g.addEdge("A", "E")
    g.addEdge("B", "E")
    g.addEdge("C", "B")
    g.addEdge("C", "D")
    # g.removeNode("A")
    # g.removeNode("B")
    # g.removeEdge("A", "C")
    g.print_()
    print(g.BFS("C"))
    print(g.DFS("C"))
    G = Graph()
    G.addNode("X")
    G.addNode("A")
    G.addNode("B")
    G.addNode("P")
    G.addEdge("X", "A")
    G.addEdge("X", "B")
    G.addEdge("A", "P")
    G.addEdge("B", "P")
    print(G.toplogicalSort())
