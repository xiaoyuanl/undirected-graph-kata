class UserInput():
    def __init__(self, graph):
        self.graph = graph

    def _tokenize(self, string):
        tokens = string.split()

        if not (len(tokens) % 2 == 0):
            raise self.OddNumberOfEdges(len(tokens))

        return tokens

    def interpret(self, string):
        try:
            tokens = self._tokenize(string)

            for a, b in tokens:
                self.insert_vertex(a, b)

            qty_disconnected = self.graph.disconnected_sub_graphs()
        except self.graph.VertexDoesNotExist as e:
            print("The requested vertex does not exist: %s" % e)
        except self.OddNumberOfEdges as e:
            print("Odd number of edges provided: %s" % e)
        except Exception as e:
            print("General exception: %s" % e)

        return qty_disconnected

class OddNumberOfEdges(ValueError):
    """To correctly add vertexes, the quantity of edges must be even."""

UserInput.OddNumberOfEdges = OddNumberOfEdges
