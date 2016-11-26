import unittest

from undirected_graph import main
from undirected_graph.user_input import UserInput
from undirected_graph.graph import Graph

class TestMain(unittest.TestCase):
    def setUp(self):
        graph = Graph()
        self.user_input = UserInput(graph)

    def test_providesValidFinalResult_one(self):
        edges = '1 2 2 3 2 4 2 5 2 6 2 7'
        result = self.user_input.interpret(edges)
        self.assertEqual(result, 1)

    def test_providesValidFinalResult_two(self):
        edges = '1 2 2 3 3 1 4 5'
        result = self.user_input.interpret(edges)
        self.assertEqual(result, 2)

    def test_providesValidFinalResult_four(self):
        edges = '1 2 2 3 3 1 9 9 8 8 7 6 5 8'
        result = self.user_input.interpret(edges)
        self.assertEqual(result, 4)
