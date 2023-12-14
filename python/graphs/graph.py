from __future__ import annotations
from typing import Any, Type, Tuple
from linked_lists.singly_linked_list import SinglyLinkedList
from queues.queue import Queue
from stacks.stack import Stack

class Graph:
    """A class modeling a simple, directed, unweighted graph."""

    class Vertex:
        """A class representing a vertex in a graph. Vertices are identified by a unique key."""

        def __init__(self, key: Any):
            """Initialize a Vertex instance. 
            
            Parameters:
                key: The unique identifier for this vertex.
            
            """
            self.id = key
            self._adj_list = SinglyLinkedList()

        def __eq__(self, other: Type[Graph.Vertex]):
            return self.id == other.id

        def __hash__(self) -> int:
            return hash(repr(self)) # pragma: no cover

        def __repr__(self) -> str:
            return f'Vertex({repr(self.id)})'

        def __str__(self) -> str:
            return f'<{str(self.id)}>'

        def has_edge_to(self, destination_vertex: Type[Graph.Vertex]) -> bool:
            """Check if there is an edge from this vertex to the destination vertex.

            Parameters:
                destination_vertex (Vertex): The destination vertex.

            Returns:
                bool: True if there is an edge from this vertex to the destination, False otherwise.
            """
            return self._adj_list.search(lambda v: v == destination_vertex) is not None

        def add_edge_to(self, destination_vertex: Type[Graph.Vertex]) -> None:
            """Add an edge from this vertex to the destination vertex.
            
            Parameters:
                destination_vertex (Vertex): The destination vertex.
            """
            if self.has_edge_to(destination_vertex):
                raise ValueError(f'Edge already exists: {self} -> {destination_vertex}')
            self._adj_list.insert_in_front(destination_vertex)

        def delete_edge_to(self, destination_vertex: Type[Graph.Vertex]):
            """Remove the edge from this vertex to the destination vertex, if it exists.

            Parameters:
                destination_vertex (Vertex): The destination vertex.
            """
            try:
                self._adj_list.delete(destination_vertex)
            except ValueError as e:
                raise ValueError(f'Edge does not exist: {self} -> {destination_vertex}') from e

        def outgoing_edges(self) -> list[Tuple[Any, Any]]:
            """Get a list of outgoing edges from this vertex.

            Returns:
                list[Tuple[Any, Any]]: A list of tuples of the form (source, destination).
                    For both vertices we return their keys.
            """
            return [(self.id, v.id) for v in self._adj_list]


    def __init__(self):
        self._adj = {}


    def __repr__(self) -> str:
        def edges_repr(edges):
            return f"[{', '.join((f'->{u}' for (_, u) in edges))}]"

        adj_lst_repr = (f'{repr(v)}: {edges_repr(v.outgoing_edges())}' for v in self._adj.values())
        return f'Graph({" | ".join(adj_lst_repr)})'


    def _get_vertex(self, key: Any) -> Type[Graph.Vertex]:
        if key not in self._adj:
            raise ValueError(f'Vertex {key} does not exist!')
        return self._adj[key]


    def insert_vertex(self, key: Any) -> None:
        """Add a vertex to the graph.
        
        Parameters:
            key: The unique identifier of the vertex to add.

        Raises:
           ValueError: If the vertex already exists.
        """
        if key in self._adj:
            raise ValueError(f'Vertex {key} already exists!')
        self._adj[key] = Graph.Vertex(key)


    def has_vertex(self, key: Any) -> bool:
        """Check if the graph contains a vertex with the given key.

        Parameters:
            key: The unique identifier of the vertex to check.

        Returns:
            bool: True if the graph contains a vertex with the given key, False otherwise.
        """
        return key in self._adj


    def delete_vertex(self, key: Any) -> None:
        """Delete a vertex from the graph.
        
        Parameters:
            key: The unique identifier of the vertex to delete.
            
        Raises:
            ValueError: If no vertex with the given key exists.
        
        """
        v = self._get_vertex(key)
        for u in self._adj.values():
            if u != v and u.has_edge_to(v):
                u.delete_edge_to(v)
        del self._adj[key]


    def get_vertices(self) -> set[Any]:
        """Get a list of the unique identifiers of all vertices in the graph.

        Returns:
            set[Any]: A list of the unique identifiers of all vertices in the graph.
        """
        return set(self._adj.keys())


    def vertex_count(self) -> int:
        """Get the number of vertices in the graph.

        Returns:
            int: The number of vertices in the graph.
        """
        return len(self._adj)


    def insert_edge(self, key1: Any, key2: Any) -> None:
        """Add an edge between two vertices in the graph.
        
        Parameters:
            key1: The unique identifier of the first vertex.
            key2: The unique identifier of the second vertex.
        
        Raises:
            ValueError: If the edge already exists.
        """
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        v1.add_edge_to(v2)


    def has_edge(self, key1: Any, key2: Any) -> bool:
        """Check if the graph contains an edge between two vertices.

        Parameters:
            key1: The unique identifier of the first vertex.
            key2: The unique identifier of the second vertex.

        Returns:
            bool: True if the graph contains an edge between the two vertices, False otherwise.

        Raises:
            ValueError: If any of the vertices does not exist.
        """
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        return v1.has_edge_to(v2)


    def delete_edge(self, key1: Any, key2: Any) -> None:
        """Delete an edge between two vertices in the graph.

        Parameters:
            key1: The unique identifier of the first vertex.
            key2: The unique identifier of the second vertex.
        
        Raises:
            ValueError: If the edge does not exist, or any of the vertices does not exist.
        """
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        v1.delete_edge_to(v2)


    def get_edges(self) -> set[tuple[Any, Any]]:
        """Get a list of all edges in the graph.

        Returns:
            set[tuple[Any, Any]]: A list of all edges in the graph. 
                Each edge is returned as a (source, destination) pair of vertex keys.
        """
        return set(e for v in self._adj.values() for e in v.outgoing_edges())


    def edge_count(self) -> int:
        """Get the number of edges in the graph.

        Returns:
            int: The number of edges in the graph.
        """
        return sum(len(v.outgoing_edges()) for v in self._adj.values())


    def bfs(self, start_vertex: Any, target_vertex: Any) -> list[Any]:
        """Perform a breadth-first search from a given vertex.
           Looks for the shortest path from the start vertex to the target vertex.

        Parameters:
            start_vertex: The unique identifier of the start vertex.
            target_vertex: The unique identifier of the target vertex.
        
        Returns:
        list[Any]: A list of vertex keys representing the shortest path from the start vertex 
            to the target vertex.
        """
        if not self.has_vertex(start_vertex):
            raise ValueError(f'Start vertex {start_vertex} does not exist!')
        if not self.has_vertex(target_vertex):
            raise ValueError(f'Target vertex {target_vertex} does not exist!')

        def reconstruct_path(pred: dict[Any, Any], target: Any) -> list[Any]:
            # Reconstruct the path from start to target by going back until it finds a vertex
            # without predecessor: That can only be the start vertex
            path = []
            while target:
                path.append(target)
                target = pred[target]
            return path[::-1]

        distance = {v: float('inf') for v in self._adj}
        predecessor = {v: None for v in self._adj}

        queue = Queue(self.vertex_count())
        # Initially, we add the start vertex to the queue
        queue.enqueue(start_vertex)
        distance[start_vertex] = 0

        while not queue.is_empty():
            u = queue.dequeue()
            if u == target_vertex:
                # We have found the shortest path to the target
                return reconstruct_path(predecessor, target_vertex)

            # For each of u's neighbors, we check if there was already a shorter path to them
            for (_, v) in self._get_vertex(u).outgoing_edges():
                if distance[v] == float('inf'):
                    distance[v] = distance[u] + 1
                    predecessor[v] = u
                    queue.enqueue(v)

        #At this point, we know there is no path from the start to the target vertex
        return None

    def dfs(self, start_vertex: Any, color: dict[Any, str] = None) -> Tuple[bool, dict[Any, str]]:
        """Perform a depth-first search from a given vertex.
           Looks for the shortest path from the start vertex to the target vertex.

        Parameters:
            start_vertex: The unique identifier of the start vertex.
            color: A dictionary mapping vertices to colors. If not provided,
                a new dictionary is created.

        Returns:
            Tuple[bool, dict[Any, str]]: A tuple containing a boolean indicating whether the graph
                is acyclic, and the up-to-date dictionary mapping vertices to colors.
        """
        if not self.has_vertex(start_vertex):
            raise ValueError(f'Start vertex {start_vertex} does not exist!')
        if color is None:
            color = {v: 'white' for v in self._adj}
        acyclic = True
        stack = Stack()
        stack.push((False, start_vertex))
        while not stack.is_empty():
            (mark_as_black, v) = stack.pop()
            col = color.get(v, 'white')
            if mark_as_black:
                color[v] = 'black'
            elif col == 'grey':
                acyclic = False
            elif col == 'white':
                color[v] = 'grey'
                stack.push((True, v))
                for (_, w) in self._get_vertex(v).outgoing_edges():
                    stack.push((False, w))
        return acyclic, color
