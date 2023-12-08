from typing import Any, Type
from linked_lists.singly_linked_list import SinglyLinkedList

class Graph:

    class Vertex:
        """A class representing a vertex in a graph. Vertices are identified by a unique key."""

        def __init__(self, key: Any):
            """Initialize a Vertex instance. 
            
            Parameters:
                key: The unique identifier for this vertex.
            
            """
            self._id = key
            self._adj_list = SinglyLinkedList()

        def __eq__(self, other: Type[Graph.Vertex]):
            return self._id == other._id

        def __hash__(self) -> int:
            return hash(repr(self))

        def __repr__(self) -> str:
            return f'Vertex({repr(self._id)})'

        def __str__(self) -> str:
            return f'<{str(self._id)}>'


    def __init__(self):
        self._adj = {}


    def add_vertex(self, key: Any) -> None:
        """Add a vertex to the graph.
        
        Raises an error if the vertex already exists.
        """
        if key in self._adj:
            raise ValueError(f'Vertex {key} already exists!')
        self._adj[key] = Graph.Vertex(key)


    def add_edge(self, v1: Any, v2: Any) -> None:
        pass

    def _get_vertex(self, key: Any) -> Type[Graph.Vertex]:
        if key not in self._adj: 
            raise ValueError(f'Vertex {key} does not exist!')
        return self._adj[key]
