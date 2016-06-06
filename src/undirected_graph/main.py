from undirected_graph.user_input import UserInput
from undirected_graph.graph import Graph

def main():
    graph = Graph()
    user_input = UserInput(graph)

    while True:
        edges = input('edges> ')
        print(user_input.interpret(edges))
