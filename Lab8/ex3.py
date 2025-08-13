class UnionFind:
    def __init__(self, n):
        # Initializing parent array
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Recursively find the root parent of x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of x and y
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False  # cycle detected, union not performed

        # Union by rank to keep tree balanced
        # Attach smaller tree under the root of larger tree
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True  # Union successfull therefor no cycle created

class Graph:
    def __init__(self, vertices):
        # Initializing graph with number of vertices
        self.V = vertices
        # Store edges as a list of tuples
        self.edges = []

    def add_edge(self, u, v, w):
        # Add an undirected weighted edge between vertices u and v
        self.edges.append((u, v, w))

    def mst(self):
        # This method returns a new Graph object representing the MST
        # Sort all edges by weight in non-decreasing order
        self.edges.sort(key=lambda x: x[2])

        # Initialize Union by finding structure for cycle detection
        uf = UnionFind(self.V)

        # Create a new Graph to store the MST edges
        mst_graph = Graph(self.V)

        # Iterate over all sorted edges
        for u, v, w in self.edges:
            # Check if the current edge connects two disconnected sets
            if uf.union(u, v):
                # If union was successful, add edge to MST
                mst_graph.add_edge(u, v, w)

                # If MST has (V-1) edges, it's complete
                if len(mst_graph.edges) == self.V - 1:
                    break

        # Return the MST graph object
        return mst_graph

    def print_graph(self):
       labels = ['A', 'B', 'C', 'D', 'E', 'F']
        # Helper method to print edges in the graph
       for u, v, w in mst_graph.edges:
            print(f"{labels[u]}-{labels[v]} = {w}")

g = Graph(6)
g.add_edge(0, 1, 4)  
g.add_edge(0, 2, 3)  
g.add_edge(1, 2, 1)  
g.add_edge(1, 3, 2)  
g.add_edge(2, 3, 4)  
g.add_edge(2, 4, 2)  
g.add_edge(3, 4, 3)  
g.add_edge(3, 5, 2)  
g.add_edge(4, 5, 3)  

mst_graph = g.mst()
mst_graph.print_graph()
