"""
Undirected Graph representation using adjacency list
Adjacency list will be represented as a dictionary having vertices as key and
a list of adjacent vertices as value.
"""

class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adj_list = self.make_adjacency_list()

    def make_adjacency_list(self):
        adj_list = {}
        for vertex in self._vertices:
            adj_list[vertex] = []
        return adj_list

    def print_adj_list(self):
        for vertex in self._vertices:
            print(vertex, "->", self._adj_list[vertex])

    def insert_edge(self, start_vertex, end_vertex):
        if start_vertex != end_vertex:
            self._adj_list[start_vertex].append(end_vertex)
            self._adj_list[end_vertex].append(start_vertex)

    def find_adjacent_nodes(self, vertex):
        return self._adj_list[vertex]

    def is_connected(self, vertex1, vertex2):
        return vertex2 in self._adj_list[vertex1]


if __name__ == "__main__":
    vertices = ["A", "B", "C", "D", "E", "F", "G", "H"] # vertices list
    graph = Graph(vertices)
    graph.insert_edge("A", "B")
    graph.insert_edge("A", "C")
    graph.insert_edge("A", "D")
    graph.insert_edge("B", "E")
    graph.insert_edge("B", "F")
    graph.insert_edge("C", "G")
    graph.insert_edge("D", "H")
    graph.insert_edge("E", "H")
    graph.insert_edge("F", "H")
    graph.insert_edge("G", "H")

    graph.print_adj_list()

    # Find all the adjacent nodes
    print("Adjacent vertices to H are: {}".format(graph.find_adjacent_nodes("H"))) # ['D', 'E', 'F', 'G']

    # Find if two nodes are connected
    print("Are Vertex A and Vertex H connected? - {}".format(graph.is_connected("A", "H"))) # false
