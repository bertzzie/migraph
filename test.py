import random
import unittest

from migraph import MiGraph


class TestMiGraphVertex(unittest.TestCase):
    def setUp(self):
        self.graph = MiGraph()

    def tearDown(self):
        self.graph.clear_graph()

    def test_addVertex(self):
        self.graph.add_vertex('a')
        self.assertTrue('a' in self.graph.vertices())

        self.graph.add_vertex('b')
        self.assertTrue('b' in self.graph.vertices())

    def test_addVertices(self):
        self.graph.add_vertices(['c', 'd', 'e'])
        self.assertTrue('c' in self.graph.vertices())
        self.assertTrue('d' in self.graph.vertices())
        self.assertTrue('e' in self.graph.vertices())

    def test_isAdjacent(self):
        self.graph.clear_graph()
        vertices = ['a', 'b', 'c', 'd']
        edges    = [('a', 'b', 10), ('b', 'd', 2)]
        self.graph.add_vertices(vertices)
        self.graph.add_edges(edges)

        self.assertTrue(self.graph.is_adjacent('a', 'b'))
        self.assertTrue(self.graph.is_adjacent('b', 'd'))
        self.assertFalse(self.graph.is_adjacent('c', 'd'))

    def test_removeVertex(self):
        self.graph.clear_graph()
        vertices = ['a', 'b', 'c', 'd']
        edges    = [('b', 'c', 10), ('b', 'd', 2)]
        self.graph.add_vertices(vertices)

        self.graph.remove_vertex('a')
        self.graph.remove_vertex('c')

        self.assertFalse('a' in self.graph.vertices())
        self.assertFalse('c' in self.graph.vertices())
        self.assertFalse(self.graph.is_adjacent('b', 'c'))

class TestMiGraphEdge(unittest.TestCase):
    def setUp(self):
        self.graph = MiGraph()

    def tearDown(self):
        self.graph = None

    def test_addEdgeWrongParam(self):
        self.assertRaises(ValueError, self.graph.add_edge, ())
        self.assertRaises(ValueError, self.graph.add_edge, ('a'))
        self.assertRaises(ValueError, self.graph.add_edge, ('a', 'b'))
        self.assertRaises(ValueError, self.graph.add_edge, ('a', 'b', 'c', 'd'))

    def test_addEdge(self):
        self.graph.add_edge(('a', 'b', 3))

        self.assertTrue({'a', 'b'} in self.graph.edges())
        self.assertEqual(self.graph.get_neighbour_weight('a', 'b'), 3)

    def test_addEdges(self):
        edges = [('a', 'c', 2), ('b', 'd', 3)]
        self.graph.add_edges(edges)

        self.assertTrue({'a', 'c'} in self.graph.edges())
        self.assertTrue({'b', 'd'} in self.graph.edges())
        self.assertEqual(self.graph.get_neighbour_weight('a', 'c'), 2)
        self.assertEqual(self.graph.get_neighbour_weight('b', 'd'), 3)

    def test_neighbourNotExists(self):
        self.graph.add_vertices(['a', 'b', 'c', 'd'])

        self.assertRaises(ValueError, self.graph.get_neighbour, 'z')

    def test_neighbour(self):
        self.graph.add_vertices(['a', 'b', 'c', 'd'])
        self.graph.add_edge(('a', 'b', 2))
        self.graph.add_edge(('a', 'c', 4))

        self.assertTrue('b' in self.graph.get_neighbour('a'))
        self.assertTrue('c' in self.graph.get_neighbour('a'))

    def test_neighbour_weightNotExists(self):
        self.graph.add_vertices(['a', 'b', 'c', 'd'])
        self.graph.add_edge(('a', 'b', 2))

        self.assertRaises(ValueError, self.graph.get_neighbour_weight, 'a', 'z')

    def test_neighbour_weight(self):
        self.graph.add_vertices(['a', 'b', 'c', 'd'])
        self.graph.add_edge(('a', 'b', 2))
        self.graph.add_edge(('a', 'c', 4))

        self.assertEqual(self.graph.get_neighbour_weight('a', 'b'), 2)
        self.assertEqual(self.graph.get_neighbour_weight('a', 'c'), 4)

    def test_removeEdge(self):
        self.graph.add_vertices(['a', 'b', 'c', 'd'])
        self.graph.add_edge(('a', 'b', 2))
        self.graph.add_edge(('a', 'c', 4))
        self.assertTrue(self.graph.is_adjacent('a', 'b'))
        self.graph.remove_edge('a', 'b')
        self.assertFalse(self.graph.is_adjacent('a', 'b'))

class TestMiGraphTraversal(unittest.TestCase):
    def setUp(self):
        self.graph = MiGraph()

    def tearDown(self):
        self.graph = None

    def test_BFS(self):
        self.graph.clear_graph()
        vertices = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o']
        edges    = [
            ('a', 'b', 1),('a', 'c', 1),
            ('b','d',1),('b','e',1),
            ('d','h',1),('d','i',1),
            ('e','j',1),('e','k',1),
            ('c','f',1),('c','g',1),
            ('f','l',1),('f','m',1),
            ('g','n',1),('g','o',1)
            ]
        self.graph.add_vertices(vertices)
        self.graph.add_edges(edges)
        print("BFS")
        print(self.graph.BFS_traversal('a'))

    def test_DFS(self):
        self.graph.clear_graph()
        vertices = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o']
        edges    = [
            ('a', 'b', 1),('a', 'c', 1),
            ('b','d',1),('b','e',1),
            ('d','h',1),('d','i',1),
            ('e','j',1),('e','k',1),
            ('c','f',1),('c','g',1),
            ('f','l',1),('f','m',1),
            ('g','n',1),('g','o',1)
            ]
        self.graph.add_vertices(vertices)
        self.graph.add_edges(edges)
        print("DFS")
        print(self.graph.DFS_traversal('a'))

if __name__ == '__main__':
    unittest.main()
