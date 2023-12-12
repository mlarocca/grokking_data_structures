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


    def create_bfs_disconnected_graph(self):
        graph = Graph()
        graph.insert_vertex(1)
        graph.insert_vertex(2)
        graph.insert_vertex(3)
        graph.insert_vertex(4)
        graph.insert_vertex(5)
        graph.insert_edge(1, 2)
        graph.insert_edge(1, 3)
        graph.insert_edge(2, 3)
        graph.insert_edge(2, 4)
        graph.insert_edge(3, 5)
        graph.insert_edge(4, 1)

        graph.insert_vertex(6)
        graph.insert_vertex(7)
        graph.insert_vertex(8)
        graph.insert_edge(6, 7)

        self.assertEqual(graph.vertex_count(), 8)
        self.assertEqual(graph.edge_count(), 7)
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


    def test_bfs(self):
        graph = self.create_bfs_disconnected_graph()
        result = graph.bfs(4, 3)
        self.assertListEqual(result, [4, 1, 3])

        result = graph.bfs(4, 5)
        self.assertListEqual(result, [4, 1, 3, 5])

        result = graph.bfs(2, 1)
        self.assertListEqual(result, [2, 4, 1])

        result = graph.bfs(1, 6)
        self.assertIsNone(result)


    def test_bfs_invalid_arguments(self):
        graph = self.create_test_graph()
        with self.assertRaises(ValueError):
            graph.bfs('Invalid', 1)

        with self.assertRaises(ValueError):
            graph.bfs(1, 'Invalid')


    def test_dfs_invalid_arguments(self):
        graph = self.create_test_graph()
        with self.assertRaises(ValueError):
            graph.dfs('Invalid')

        with self.assertRaises(ValueError):
            graph.dfs('Invalid', {})


    def test_dfs(self):
        graph = self.create_bfs_disconnected_graph()
        acyclic, color = graph.dfs(4)
        self.assertFalse(acyclic)
        self.assertEqual(color, {1: 'black',
                                 2: 'black',
                                 3: 'black',
                                 4: 'black',
                                 5: 'black',
                                 6: 'white',
                                 7: 'white',
                                 8: 'white'})

        acyclic, color = graph.dfs(2)
        self.assertFalse(acyclic)
        self.assertEqual(color, {1: 'black',
                                 2: 'black',
                                 3: 'black',
                                 4: 'black',
                                 5: 'black',
                                 6: 'white',
                                 7: 'white',
                                 8: 'white'})

        acyclic, color = graph.dfs(3)
        self.assertTrue(acyclic)
        self.assertEqual(color, {1: 'white',
                                 2: 'white',
                                 3: 'black',
                                 4: 'white',
                                 5: 'black',
                                 6: 'white',
                                 7: 'white',
                                 8: 'white'})

        acyclic, color = graph.dfs(6)
        self.assertTrue(acyclic)
        self.assertEqual(color, {1: 'white',
                                 2: 'white',
                                 3: 'white',
                                 4: 'white',
                                 5: 'white',
                                 6: 'black',
                                 7: 'black',
                                 8: 'white'})

        acyclic, color = graph.dfs(3)
        self.assertTrue(acyclic)
        self.assertEqual(color, {1: 'white',
                                 2: 'white',
                                 3: 'black',
                                 4: 'white',
                                 5: 'black',
                                 6: 'white',
                                 7: 'white',
                                 8: 'white'})

        # Test passing the color dictionary as second argument
        acyclic, color = graph.dfs(2)
        self.assertFalse(acyclic)
        acyclic, color = graph.dfs(6, color)
        # Note that the result refers only to what could be learned in the last call of dfs!
        self.assertTrue(acyclic)
        self.assertEqual(color, {1: 'black',
                                 2: 'black',
                                 3: 'black',
                                 4: 'black',
                                 5: 'black',
                                 6: 'black',
                                 7: 'black',
                                 8: 'white'})

        acyclic, color = graph.dfs(6)
        self.assertTrue(acyclic)
        acyclic, color = graph.dfs(2, color)
        self.assertFalse(acyclic)
        self.assertEqual(color, {1: 'black',
                                 2: 'black',
                                 3: 'black',
                                 4: 'black',
                                 5: 'black',
                                 6: 'black',
                                 7: 'black',
                                 8: 'white'})

        graph.delete_edge(4, 1)
        acyclic, color = graph.dfs(3)
        self.assertTrue(acyclic)
        acyclic, color = graph.dfs(2, color)
        self.assertTrue(acyclic)
        self.assertEqual(color, {1: 'white',
                                 2: 'black',
                                 3: 'black',
                                 4: 'black',
                                 5: 'black',
                                 6: 'white',
                                 7: 'white',
                                 8: 'white'})
