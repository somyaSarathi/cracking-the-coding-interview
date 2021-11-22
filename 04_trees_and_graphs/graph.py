class graph:
    def __init__(self) -> None:
        self.vertices: dict = dict()
        self.weights: dict = dict()
        return

    def addVertex(self, vertex, edges: list=[], weights: list=[]) -> None:
        if not edges:
            try:
                self.vertices[vertex]
            except KeyError:
                self.vertices[vertex] = set()
            return

        if edges and weights:
            if len(edges) < len(weights):
                raise ValueError

        try:
            for i in range(len(edges)):
                self.vertices[vertex].add(edges[i])
                try:
                    self.weights[(vertex, edges[i])] = weights[i]
                    self.addVertex(edges[i])
                except IndexError:
                    self.weights[(vertex, edges[i])] = 1
                    self.addVertex(edges[i])

        except KeyError:
            self.vertices[vertex] = set()
            for i in range(len(edges)):
                self.vertices[vertex].add(edges[i])
                try:
                    self.weights[(vertex, edges[i])] = weights[i]
                    self.addVertex(edges[i])
                except IndexError:
                    self.weights[(vertex, edges[i])] = 1
                    self.addVertex(edges[i])
        
        return


    def deleteVertex(self, vertex):
        try:
            del self.vertices[vertex]
            for edges in self.vertices.values():
                edges.remove(vertex)

        except KeyError:
            return
