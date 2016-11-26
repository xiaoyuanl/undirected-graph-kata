import unittest

from undirected_graph.graph import Graph
from undirected_graph.user_input import UserInput

class TestUserInput(unittest.TestCase):
    def test_userInputClassExists(self):
        self.assertTrue(UserInput is not None)

    def setUp(self):
        self.graph = Graph()
        self.user_input = UserInput(self.graph)

    def test_userInputTakesGraphObjectInConstructor(self):
        self.assertTrue(self.user_input.graph is not None)

    def test_tokenizeMethodReturnsAList(self):
        input = '1 2 2 3 3 1 4 5'
        result = self.user_input._tokenize(input)
        self.assertTrue(type(result) is list)
        self.assertEqual(len(result), 8)

    def test_tokenizeMethodReturnsCorrectQty(self):
        input = '1 2 2 3 3 1 4 5'
        result = self.user_input._tokenize(input)
        self.assertEqual(len(result), 8)

    def test_tokenizeRequiresEvenNumberOfEdges(self):
        input = '1 2 3'
        self.assertRaises(
            self.user_input.OddNumberOfEdges,
            self.user_input._tokenize, input
        )

    def test_insertVertexesAddsCorrectQtyOfVertexes(self):
        input = '1 2 3 4'
        tokens = self.user_input._tokenize(input)
        vertex_qty = self.user_input._insert_multiple_vertexes(tokens)
        self.assertEqual(vertex_qty, 4)
