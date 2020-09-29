class Helper:
    def __init__(self):
        self._vertices_index = {}

    def make_vertices_index(self, vertices):
        for index, vertex in enumerate(vertices):
            self._vertices_index[vertex] = index

    def get_index_for_vertex(self, vertex):
        return self._vertices_index[vertex]

class Graph:
    def __init__(self, vertices, helper):
        self._helper = helper
        num_of_vertices = len(vertices)
        self._adj_matrix = [[ 0 for col in range(num_of_vertices)] for row in range(num_of_vertices)]

    def print_adj_matrix(self):
        print(self._adj_matrix)

    def insert_edge(self, start_vertex, end_vertex):
        # for undirected graph we don't need weight for any edge
        start_vertex_index = self._helper.get_index_for_vertex(start_vertex)
        end_vertex_index = self._helper.get_index_for_vertex(end_vertex)

        if start_vertex_index != end_vertex_index:
            self._adj_matrix[start_vertex_index][end_vertex_index] = 1
            self._adj_matrix[end_vertex_index][start_vertex_index] = 1


if __name__ == "__main__":
    vertices = ["A", "B", "C", "D", "E", "F"] # vertices list
    helper = Helper()
    helper.make_vertices_index(vertices)

    graph = Graph(vertices, helper) # create a graph

    # Add edges --> Each edge represents a connection between two vertices as A -> B and B -> A
    graph.insert_edge("A", "B")
    graph.insert_edge("A", "C")
    graph.insert_edge("A", "D")
    graph.insert_edge("B", "E")
    graph.insert_edge("B", "F")
    graph.insert_edge("C", "D")
    graph.insert_edge("D", "E")
    graph.insert_edge("E", "F")

    graph.print_adj_matrix()
    """
    Prints:
    [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 1, 0]]
    """
