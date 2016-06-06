class Graph():
    def __init__(self):
        self.adjacencies = {}

    def insert_vertex(self, a, b):
        if a not in self.adjacencies:
            self.adjacencies[a] = set()
        self.adjacencies[a].add(b)

        if b not in self.adjacencies:
            self.adjacencies[b] = set()
        self.adjacencies[b].add(a)

    def remove_vertex(self, a):
        if a not in self.adjacencies:
            raise self.VertexDoesNotExist(a)

        neighbors = self.adjacencies[a]
        is_vertex_loop = (a in neighbors)

        if is_vertex_loop:
            self.adjacencies[a].remove(a)

        for vertex in neighbors:
            self.adjacencies[vertex].remove(a)

        del self.adjacencies[a]

    def disconnected_sub_graphs(self):
        adjacencies = self.adjacencies
        queued = []
        qty = 0

        while adjacencies:
            qty += 1
            initial_vertex = list(adjacencies.keys())[0]

            neighbors = list(adjacencies[initial_vertex])
            queued = queued + neighbors

            self.remove_vertex(initial_vertex)

            while queued:
                vertex = queued.pop()
                if vertex in adjacencies:
                    neighbors = list(adjacencies[vertex])
                    queued = queued + neighbors
                    self.remove_vertex(vertex)

        return qty

class VertexDoesNotExist(KeyError):
    """When a requested vertex name could not be found."""

Graph.VertexDoesNotExist = VertexDoesNotExist
