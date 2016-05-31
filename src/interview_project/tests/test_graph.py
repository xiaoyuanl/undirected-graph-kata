import unittest
import ipdb
from interview_project.graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_insertVertexKeyExistance(self):
        self.graph.insert_vertex('a', 'b')
        self.assertTrue('a' in self.graph.adjacencies)
        self.assertTrue('b' in self.graph.adjacencies)

    def test_insertVertexValueExistance(self):
        self.graph.insert_vertex('a', 'b')
        self.graph.insert_vertex('a', 'c')
        self.assertTrue('b' in self.graph.adjacencies['a'])
        self.assertTrue('c' in self.graph.adjacencies['a'])

    def test_removeVertexKeyExistance(self):
        self.graph.insert_vertex('a', 'b')
        self.graph.insert_vertex('c', 'a')
        self.graph.remove_vertex('a')
        self.assertTrue('a' not in self.graph.adjacencies)

    def test_removeVertexValueExistance(self):
        self.graph.insert_vertex('a', 'b')
        self.graph.insert_vertex('c', 'a')
        self.graph.remove_vertex('a')
        self.assertTrue('a' not in self.graph.adjacencies['b'])
        self.assertTrue('a' not in self.graph.adjacencies['c'])

    def test_removeVertexDoesNotExist(self):
        self.graph.insert_vertex('a', 'b')
        self.assertRaises(
            self.graph.VertexDoesNotExist,
            self.graph.remove_vertex, 'z'
        )

    def test_singleEdgeOnOneGraph(self):
        self.graph.insert_vertex('a', 'b')
        self.assertEqual(self.graph.disconnected_sub_graphs(), 1)

    def test_singleLoopbackVertexOnOneGraph(self):
        self.graph.insert_vertex('a', 'a')
        self.assertEqual(self.graph.disconnected_sub_graphs(), 1)

    def test_twoLoopbackVertexesOnTwoGraphs(self):
        self.graph.insert_vertex('a', 'a')
        self.graph.insert_vertex('y', 'y')
        self.assertEqual(self.graph.disconnected_sub_graphs(), 2)

    def test_twoEdgesOnOneGraph(self):
        self.graph.insert_vertex('a', 'b')
        self.graph.insert_vertex('c', 'b')
        self.assertEqual(self.graph.disconnected_sub_graphs(), 1)

    def test_singleEdgeForTwoGraphs(self):
        self.graph.insert_vertex('a', 'b')
        self.graph.insert_vertex('x', 'y')
        self.assertEqual(self.graph.disconnected_sub_graphs(), 2)

    def test_twoEdgesForTwoGraphs(self):
        self.graph.insert_vertex('a', 'b')
        self.graph.insert_vertex('a', 'c')
        self.graph.insert_vertex('x', 'y')
        self.graph.insert_vertex('w', 'y')
        self.assertEqual(self.graph.disconnected_sub_graphs(), 2)
