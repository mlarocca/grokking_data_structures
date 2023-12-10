import unittest
from graphs.graph import Graph

class TestGraph(unittest.TestCase):

    def create_test_graph(self):
        graph = Graph()
        graph.insert_vertex(1)
        graph.insert_vertex(0.23)
        graph.insert_vertex('ABC')
        graph.insert_vertex('WXYZ')
        graph.insert_edge('ABC', 'WXYZ')
        graph.insert_edge(1, 'ABC')
        graph.insert_edge(1, 'WXYZ')
        graph.insert_edge(1, 0.23)
        graph.insert_edge(0.23, 'ABC')
        graph.insert_edge(0.23, 1)

        self.assertEqual(graph.vertex_count(), 4)
        self.assertEqual(graph.edge_count(), 6)
        self.assertTrue(graph.has_edge('ABC', 'WXYZ'))
        self.assertTrue(graph.has_edge(1, 'ABC'))
        self.assertTrue(graph.has_edge(1, 'WXYZ'))
        self.assertTrue(graph.has_edge(1, 0.23))
        self.assertTrue(graph.has_edge(0.23, 1))
        self.assertTrue(graph.has_edge(0.23, 'ABC'))
        return graph


    def test_repr(self):
        graph = Graph()
        self.assertEqual(repr(graph), 'Graph()')
        graph.insert_vertex('A')
        self.assertEqual(repr(graph), 'Graph(Vertex(\'A\'): [])')


    def test_insert_vertex(self):
        graph = Graph()
        self.assertEqual(graph.vertex_count(), 0)
        self.assertEqual(graph.edge_count(), 0)
        self.assertFalse(graph.has_vertex(1))
        self.assertFalse(graph.has_vertex('ABC'))
        graph.insert_vertex(1)
        self.assertEqual(graph.vertex_count(), 1)
        graph.insert_vertex('ABC')
        self.assertEqual(graph.vertex_count(), 2)
        self.assertTrue(graph.has_vertex(1))
        self.assertTrue(graph.has_vertex('ABC'))


    def test_insert_existing_vertex(self):
        graph = Graph()
        self.assertEqual(graph.vertex_count(), 0)
        self.assertFalse(graph.has_vertex(1))
        graph.insert_vertex(1)
        self.assertTrue(graph.has_vertex(1))
        with self.assertRaises(ValueError):
            graph.insert_vertex(1)
        self.assertEqual(graph.vertex_count(), 1)
        self.assertTrue(graph.has_vertex(1))


    def test_insert_edge(self):
        graph = Graph()
        self.assertEqual(graph.vertex_count(), 0)
        self.assertEqual(graph.edge_count(), 0)
        graph.insert_vertex(1)
        graph.insert_vertex(0.23)
        graph.insert_vertex('ABC')
        graph.insert_vertex('WXYZ')
        self.assertEqual(graph.vertex_count(), 4)
        self.assertEqual(graph.edge_count(), 0)
        self.assertFalse(graph.has_edge('ABC', 'WXYZ'))
        self.assertFalse(graph.has_edge(1, 'ABC'))
        self.assertFalse(graph.has_edge(1, 'WXYZ'))
        self.assertFalse(graph.has_edge(1, 0.23))
        self.assertFalse(graph.has_edge(0.23, 1))
        self.assertFalse(graph.has_edge(0.23, 'ABC'))

        graph.insert_edge('ABC', 'WXYZ')
        graph.insert_edge(1, 'ABC')
        graph.insert_edge(1, 'WXYZ')
        graph.insert_edge(1, 0.23)
        graph.insert_edge(0.23, 'ABC')
        graph.insert_edge(0.23, 1)

        self.assertTrue(graph.has_edge('ABC', 'WXYZ'))
        self.assertEqual(graph.edge_count(), 6)
        self.assertTrue(graph.has_edge(1, 'ABC'))
        self.assertTrue(graph.has_edge(1, 'WXYZ'))
        self.assertTrue(graph.has_edge(1, 0.23))
        self.assertTrue(graph.has_edge(0.23, 1))
        self.assertTrue(graph.has_edge(0.23, 'ABC'))


    def test_insert_edge_invalid_source(self):
        graph = Graph()
        graph.insert_vertex(1)
        self.assertTrue(graph.has_vertex(1))
        self.assertFalse(graph.has_vertex(2))
        with self.assertRaises(ValueError):
            graph.insert_edge(2, 1)

    def test_insert_edge_invalid_destination(self):
        graph = Graph()
        graph.insert_vertex(1)
        self.assertTrue(graph.has_vertex(1))
        self.assertFalse(graph.has_vertex(2))
        with self.assertRaises(ValueError):
            graph.insert_edge(1, 2)

    def test_insert_existing_edge(self):
        graph = Graph()
        graph.insert_vertex(1)
        graph.insert_vertex(2)
        self.assertTrue(graph.has_vertex(1))
        self.assertTrue(graph.has_vertex(2))
        self.assertFalse(graph.has_edge(1,2))

        graph.insert_edge(1, 2)
        self.assertEqual(graph.edge_count(), 1)
        self.assertTrue(graph.has_edge(1,2))

        with self.assertRaises(ValueError):
            graph.insert_edge(1, 2)

        self.assertEqual(graph.edge_count(), 1)
        self.assertTrue(graph.has_edge(1,2))

    def test_delete_edge(self):
        graph = self.create_test_graph()

        graph.delete_edge(1, 'ABC')
        self.assertEqual(graph.edge_count(), 5)
        self.assertFalse(graph.has_edge(1, 'ABC'))
        self.assertTrue(graph.has_edge('ABC', 'WXYZ'))
        self.assertTrue(graph.has_edge(1, 'WXYZ'))
        self.assertTrue(graph.has_edge(1, 0.23))
        self.assertTrue(graph.has_edge(0.23, 1))
        self.assertTrue(graph.has_edge(0.23, 'ABC'))

        graph.delete_edge(0.23, 1)
        self.assertEqual(graph.edge_count(), 4)
        self.assertFalse(graph.has_edge(0.23, 1))
        self.assertFalse(graph.has_edge(1, 'ABC'))
        self.assertTrue(graph.has_edge('ABC', 'WXYZ'))
        self.assertTrue(graph.has_edge(1, 'WXYZ'))
        self.assertTrue(graph.has_edge(1, 0.23))
        self.assertTrue(graph.has_edge(0.23, 'ABC'))


    def test_delete_invalid_edge(self):
        graph = Graph()
        graph.insert_vertex(1)
        graph.insert_vertex(3.14)
        graph.insert_edge(1, 3.14)
        self.assertTrue(graph.has_vertex(1))
        self.assertTrue(graph.has_vertex(3.14))
        self.assertFalse(graph.has_vertex(2))

        with self.assertRaises(ValueError):
            graph.delete_edge(1, 2)

        with self.assertRaises(ValueError):
            graph.delete_edge(2, 3.14)

        with self.assertRaises(ValueError):
            graph.delete_edge(3.14, 1)

    def test_delete_vertex(self):
        graph = self.create_test_graph()
        self.assertTrue(graph.has_vertex(1))
        self.assertTrue(graph.has_vertex(0.23))
        self.assertTrue(graph.has_vertex('ABC'))
        self.assertTrue(graph.has_vertex('WXYZ'))
        graph.delete_vertex(1)
        self.assertEqual(graph.vertex_count(), 3)
        self.assertFalse(graph.has_vertex(1))
        self.assertTrue(graph.has_vertex(0.23))
        self.assertTrue(graph.has_vertex('ABC'))
        self.assertTrue(graph.has_vertex('WXYZ'))
        self.assertEqual(graph.edge_count(), 2)
        with self.assertRaises(ValueError):
            self.assertFalse(graph.has_edge(0.23, 1))
        self.assertTrue(graph.has_edge('ABC', 'WXYZ'))
        self.assertTrue(graph.has_edge(0.23, 'ABC'))

        graph.delete_vertex('WXYZ')
        self.assertEqual(graph.vertex_count(), 2)
        self.assertFalse(graph.has_vertex(1))
        self.assertTrue(graph.has_vertex(0.23))
        self.assertTrue(graph.has_vertex('ABC'))
        self.assertFalse(graph.has_vertex('WXYZ'))
        self.assertEqual(graph.edge_count(), 1)
        self.assertTrue(graph.has_edge(0.23, 'ABC'))

        graph.delete_vertex(0.23)
        self.assertEqual(graph.vertex_count(), 1)
        self.assertFalse(graph.has_vertex(1))
        self.assertFalse(graph.has_vertex(0.23))
        self.assertTrue(graph.has_vertex('ABC'))
        self.assertFalse(graph.has_vertex('WXYZ'))
        self.assertEqual(graph.edge_count(), 0)

        graph.delete_vertex('ABC')
        self.assertEqual(graph.vertex_count(), 0)
        self.assertFalse(graph.has_vertex(1))
        self.assertFalse(graph.has_vertex(0.23))
        self.assertFalse(graph.has_vertex('ABC'))
        self.assertFalse(graph.has_vertex('WXYZ'))

        with self.assertRaises(ValueError):
            graph.delete_vertex(1)

        with self.assertRaises(ValueError):
            graph.delete_vertex('Quack')


    def test_get_vertices(self):
        graph = self.create_test_graph()
        self.assertSetEqual(graph.get_vertices(), set([1, 0.23, 'ABC', 'WXYZ']))


    def test_get_edges(self):
        graph = self.create_test_graph()
        expected_edges = set([(1, 0.23), (0.23, 1), (1, 'ABC'), (1, 'WXYZ'), ('ABC', 'WXYZ'), (0.23, 'ABC')])
        self.assertSetEqual(graph.get_edges(), expected_edges)
